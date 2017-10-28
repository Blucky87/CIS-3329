#!/usr/bin/env python
 
import socket

TCP_IP = '129.32.100.223'
TCP_PORT = 1234
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
data = s.recv(BUFFER_SIZE)
s.close()
 
print("received data:", data.decode())