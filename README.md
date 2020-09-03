# Trabalho 3 - Key-Value Store com gRPC

Esse código utiliza o protocolo gRPC para permitir que o cliente adicione uma chave e valor. Ademais, não há a implementação de buckets de dados para cada cliente, sendo assim, todos os clientes podem acessar uma base de dados comum.

## Alunos integrantes da equipe

* Henrique Freire dos Santos
* João Américo Martins Caiafa de Andrade
* Maria Verônica Santos Soares

## Professor responsáveis

* Hugo Bastos de Paula

## Instruções de utilização

Código pb2 gerado a partir do arquivo ".proto" e o comando:
```
$ protoc --proto_path=src --python_out=build src/.proto
```

