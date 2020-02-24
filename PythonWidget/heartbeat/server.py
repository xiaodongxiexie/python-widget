# coding: utf-8


import socket

BUF_SIZE = 1024
HOST = "localhost"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

client, address = server.accept()
while True:
	data = client.recv(BUF_SIZE)
	print(data.decode())
