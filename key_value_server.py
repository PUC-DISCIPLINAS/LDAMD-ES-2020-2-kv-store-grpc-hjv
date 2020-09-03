from concurrent import futures
import argparse
import grpc
import logging
import socket
import sys
import time

import key_value_ip
import key_value_pb2
import key_value_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

args = []
store = {}
peers = []


class ConfigError(Exception):
    pass


def setCustomLogger(name):
    formatter = logging.Formatter(fmt="%(asctime)s: %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(screen_handler)
    return logger


logger = setCustomLogger("KeyValueStore")


def explain(msg):
    if args.verbose:
        logger.info("%s" % msg)


def parseArgs():
    global args
    parser = argparse.ArgumentParser(description="Key-value store server.")
    parser.add_argument("peers", nargs="*", metavar="PEER",
                        help="Set peer IP address (IPv4 only!).")
    parser.add_argument("--ip", default="127.0.0.1:4000",
                        help="Set server IP address (IPv4 only!).")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Verbosely list operations performed.")
    args = parser.parse_args()

    if not key_value_ip.isValidIP(args.ip):
        raise ConfigError("not a valid IP address: '%s'" % args.ip)

    for peerIP in args.peers:
        if not key_value_ip.isValidIP(peerIP):
            raise ConfigError("not a valid peer IP address: '%s'" % peerIP)
        if peerIP != args.ip:
            if not (peerIP in peers):
                peers.append(peerIP)
                introduceOurself(peerIP)

    return args


class Storer(key_value_pb2_grpc.ClientServicer):
    def Get(self, request, context):
        key = request.key
        if key in store:
            explain("received GET request for key '{0:s}': value = '{1:s}'".format(key, store[key]))
            return key_value_pb2.GetReply(value=store[key], defined=True)
        else:
            explain("received GET request for key '%s': value = undefined" % key)
            return key_value_pb2.GetReply(value=None, defined=False)

    def Set(self, request, context):
        key = request.key
        value = request.value
        broadcast = request.broadcast
        store[key] = value
        if broadcast:
            explain("received SET request for key '{0:s}': new value = '{1:s}'".format(key, value))
            updatePeers(key, value)
        else:
            explain("received peer update for key '{0:s}': new value = '{1:s}'".format(key, value))
        return key_value_pb2.PutReply(value=value)

    def List(self, request, context):
        explain("received LIST request")
        return key_value_pb2.StoreReply(store=store)

    def RegisterWithPeer(self, request, context):
        peerIP = request.ip
        explain("received new peer registration: %s" % peerIP)
        if key_value_ip.isValidIP(peerIP):
            if (peerIP in peers) == False:
                peers.append(peerIP)
        return key_value_pb2.StoreReply(store=store)


def introduceOurself(peerIP):
    global store
    with grpc.insecure_channel(peerIP) as channel:
        stub = key_value_pb2_grpc.ClientStub(channel)
        explain("registering with peer %s..." % peerIP)
        response = stub.RegisterWithPeer(key_value_pb2.IP(ip=args.ip))
        for key in response.store:
            store[key] = response.store[key]


def updatePeers(key, value):
    for peerIP in peers:
        explain("updating peer '{0:s}': '${1:s}' = '${2:s}'".format(peerIP, key, value))
        with grpc.insecure_channel(peerIP) as channel:
            stub = key_value_pb2_grpc.ClientStub(channel)
            stub.Set(key_value_pb2.PutKey(key=key, value=value, broadcast=False))


def serve(ip):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    key_value_pb2_grpc.add_ClientServicer_to_server(Storer(), server)
    server.add_insecure_port(ip)
    print("Listening on %s..." % ip)
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    try:
        args = parseArgs()
        serve(args.ip)
    except ConfigError as e:
        print("error:"), e.args[0]
