# Trabalho 3 - Key-Value Store com gRPC

Esse trabalho aplica conhecimentos da matéria de Laboratório de Desenvolvimento de Aplicações Moveis e Distribuídas, utilizando gRPC para desenvolver um Key-Value store in memory.

<h1 align="center">
    <a href="https://grpc.io/">gRPC🔗</a>
</h1>

<p align="center"> gRPC é um serviço de alto desempenho para atender chamadas RPC (Remote Call Procedures) </p>
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

## Professor responsável

* Hugo Bastos de Paula ([hugodepaula](https://github.com/hugodepaula))

## Instruções de utilização

Código pb2 gerado a partir do arquivo ".proto" e o comando:
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. key_value.proto
```
1. Executar ```key_value_server.py```

    Opções de argumentos:
    
    * ``` -ip "valor do IP"```, se não for passado como argumento o sistema usará endereço IP padrão.
    * ``` peers "valor do IP"```, se não for passado como argumento o sistema usará endereço IP padrão.
    * ``` -verbose ou -v```, lista todas as mensagens salvas no log do servidor.  
    
2. Executar ```key_value_client.py```

    Opções de argumentos:
    
    * ``` -ip ou -i "valor do IP"```, se não for passado como argumento o sistema usará endereço IP padrão.
    * ``` -get ou - g "key"```, retorna o value salvo a key passada. 
    * ``` -put ou -p "key,value"```, salva a key e value passados 
    
        **OBS: e caso a key já tenha sido passada anteriormente o value salvo é atualizado para o novo valor.**
    * ``` -list ou -l```, lista todos os key e value salvos.
    * ``` -verbose ou -v```, lista todas as mensagens salvas no log do servidor.    
