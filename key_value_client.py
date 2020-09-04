from __future__ import print_function

import argparse
import logging
import re
import sys

import grpc

import key_value_ip
import key_value_pb2
import key_value_pb2_grpc


args = {}

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

logger = setCustomLogger("KV")

def explain(msg):
  if args.verbose:
    logger.info("%s" % msg)

def parseArgs():
    global args
    parser = argparse.ArgumentParser(description="Envia solicitacao(oes) para um servidor de key value store.")
    parser.add_argument("-ip", "-i", nargs=1, action="store")
    parser.add_argument("-get", "-g", nargs=1, action="append")
    parser.add_argument("-put", "-p", nargs=1, action="append")
    parser.add_argument("-list", "-l", action="store_true",)
    parser.add_argument("-verbose", "-v", action="store_true")
    args = parser.parse_args()

    if args.ip == None:
        args.ip = ["127.0.0.1:4000"]
    if not key_value_ip.isValidIP(args.ip[0]):
        raise ConfigError("nao eh um IP de servidor valido: '%s'" % args.ip[0])

def doGet(ip, key):
    explain("enviando requisicao GET para {0:s} com a key '{1:s}'...".format(ip[0], key))
    with grpc.insecure_channel(args.ip[0]) as channel:
        stub = key_value_pb2_grpc.ClientStub(channel)
        response = stub.Get(key_value_pb2.GetKey(key=key))
        if response.defined:
            print("\tkey = '{0:s}'\t value = '{1:s}'".format(key, response.value))
        else:
            print("'%s': indefinido" % key)

def doSet(ip, key, value):
    explain("enviando requisicao SET para {0:s} com a key '{1:s}'...".format(ip[0], key))
    with grpc.insecure_channel(args.ip[0]) as channel:
        stub = key_value_pb2_grpc.ClientStub(channel)
        stub.Set(key_value_pb2.SetKey(key=key, value=value, broadcast=True))

def doList(ip):
    explain("enviando requisicao LIST para %s..." % ip[0])
    with grpc.insecure_channel(args.ip[0]) as channel:
        stub = key_value_pb2_grpc.ClientStub(channel)
        response = stub.List(key_value_pb2.Void())
        print("Estes sao os key value salvos em %s:" % ip[0])
        for key in response.store:
            print("  - '{0:s}'='{1:s}'".format(key, response.store[key]))
        print("-- fim da listagem de key value --")

def handleGet(ip, key):
    regex = re.compile('^[a-zA-Z0-9_]+$')
    if regex.match(key) == False:
        raise ConfigError("Expressao GET incorreta: esperado '-get KEY'; recebido '-get %s'" % key)
    doGet(ip, key)

def handlePut(ip, kv):
    regex = re.compile('^([a-zA-Z0-9_]+)=([a-zA-Z0-9_]+)$')
    m = regex.match(kv)
    if m == None:
         raise ConfigError("invalid --set: expected '--set KEY=VALUE'; got '--get %s'" % kv)
    doSet(ip, m.group(1), m.group(2))

def run():
    try:
        parseArgs()
        if args.get is not None:
            for key in args.get:
                handleGet(args.ip, key[0])
        if args.put is not None:
            for kv in args.put:
                handlePut(args.ip, kv[0])
        if args.list:
            doList(args.ip)
    except ConfigError as e:
        print("error:", e.args[0])
    except grpc.RpcError as e:
        print("error: {0:s}: {1:s}".format(e.code(), e.details()))

if __name__ == '__main__':
    run()
