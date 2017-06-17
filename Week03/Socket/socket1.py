#!/usr/bin/python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
mysock.connect(('data.pr4e.org', 80))

msg = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'
# msg = 'GET /code/romeo.txt HTTP/1.1\r\nHOST: www.py4inf.com\r\n\r\n'
sent = mysock.send(msg.encode())

print(sent)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data)

mysock.close()

