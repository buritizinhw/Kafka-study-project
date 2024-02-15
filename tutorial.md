
1. Baixar o Apache Server

    ```- sudo apt install apache2```
    Ver se está funcionando 
    ```- sudo systemctl status apache2```
    Logo após, acessar o arquivo de logs em:
    ```- cd /var/log/apache2```
    ```- cat access.log```
    Inicialmente estará vazio. Após isso, no navegador acesse(sem porta):
    ```- http://localhost```

2. Configurar o Kafka
    ```- ./zookeeper-server-start.sh ../config/server.properties```
    Agora, incializar os brokers(nesse caso, vou utilizar um cluster que ja tenho previamente configurado)
    ```- ./kafka-server-start.sh ../config/server.properties```
    ```- ./kafka-server-start.sh ../config/server.properties```
    ```- ./kafka-server-start.sh ../config/server.properties2```
    Após isso, incializaremos o topic 
    ```- ./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic apachelog``` ```--create --partitions 3 -replication-factor 3```
    E o consumer
    ```- ./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic apachelog```
3. Configurar o producer em python 
    [Producer Python](kconnectorapache.py)

4. Após isso, inicializamos o script e deverá estar funcionando o consumo das mensagens de acesso ao localhost(mesmo caso utilize uma porta que nao esteja ativa) e o producer retornará que a mensagem foi enviada dando o timedate.
