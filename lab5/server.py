#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 1234
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print('received data:', data.decode())
    conn.send(data[::-1].encode())  # echo the reversed message
conn.close()
