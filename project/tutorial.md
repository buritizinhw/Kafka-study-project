
1. Baixar o Apache Server

    ```bash
    sudo apt install apache2
    ```
   
    Ver se está funcionando
   
    ```bash
    sudo systemctl status apache2
    ```
   
    Logo após, acessar o arquivo de logs em:
   
    ```bash
    cd /var/log/apache2
    ```
   
    ```bash
    cat access.log
    ```
   
    Inicialmente estará vazio. Após isso, no navegador acesse(sem porta):
   
    ```https
    http://localhost
    ```
   
3. Configurar o Kafka
    ```bash
    ./zookeeper-server-start.sh ../config/server.properties
    ```
    Agora, incializar os brokers(nesse caso, vou utilizar um cluster que ja tenho previamente configurado)
    ```bash
   ./kafka-server-start.sh ../config/server.properties
    ```
    ```bash
    ./kafka-server-start.sh ../config/server.properties1
   ```
    ```bash
    ./kafka-server-start.sh ../config/server.properties2
   ```
    Após isso, incializaremos o topic 
    ```bash
   ./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic apachelog``` ```--create --partitions 3 -replication-factor 3
    ```
    E o consumer
    ```bash
   ./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic apachelog
    ```
    
5. Configurar o producer em python 
    [Producer Python](connectorapache.py)

6. Após isso, inicializamos o script e deverá estar funcionando o consumo das mensagens de acesso ao localhost(mesmo caso utilize uma porta que nao esteja ativa, retornando o protocolo HTTP específico do erro) e o producer retornará que a mensagem foi enviada dando o timedate.
