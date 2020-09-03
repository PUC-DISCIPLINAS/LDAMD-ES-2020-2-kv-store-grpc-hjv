# Trabalho 3 - Key-Value Store com gRPC

Esse trabalho visa aplicar conhecimentos da matéria de LDAMD utilizando gRPC para desenvolver um Key-Value store in memory.

<h1 align="center">
    <a href="https://grpc.io/">🔗 gRPC</a>
</h1>

<p align="center"> gRPC é um serviço de alto desempenho para atender chamadas RPC (Remote Call Procedures). </p>
<p align="center">

## Instruções

Neste trabalho, será necessário utilizar o protocolo gRPC para permitir que o cliente adicione uma chave e valor. Neste trabalho não será necessário implementar buckets de dados para cada cliente. Ou seja, todos os clientes poderão acessar uma base de dados comum.

## Features

* put(key, value)
* get(key) : value

## Alunos integrantes da equipe

* Henrique Freire dos Santos ([henfreire](https://github.com/henfreire))
* João Américo Martins Caiafa de Andrade ([Leusd](https://github.com/Leusd))
* Maria Verônica Santos Soares ([mveronicasoares](https://github.com/mveronicasoares))

## Professor responsáveis

* Hugo Bastos de Paula ([hugodepaula](https://github.com/hugodepaula))

## Instruções de utilização

Código pb2 gerado a partir do arquivo ".proto" e o comando:
```
$ protoc --proto_path=src --python_out=build src/.proto
```

