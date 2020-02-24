# coding: utf-8


import socket
import time

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
client.connect((HOST, PORT))

while True:
	client.send(b"still alive")
	time.sleep(1)
