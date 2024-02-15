import time
import re
import datetime
from kafka import KafkaProducer as kp

archive = open(r'/var/log/apache2/access.log', 'r')

regexp = '^([\\d.]+) (\\S+) (\\S+) \\[([\\w:/]+\\s[+-]\\d{4})\\] \"(.+?)\" (\\d{3}) (\\d+) \"([^\"]+)\" \"(.+?)\"'

producer = kp(bootstrap_servers = '127.0.0.1:9092')

while 1:
    linha = archive.readline()
    if not linha:
        time.sleep(5)
    else:
        x = re.match(regexp, linha).groups()
        msg = bytes(str(x), encoding = 'ascii')
        producer.send("apachelog", msg)
        print("Message sent at ", datetime.datetime.now())

