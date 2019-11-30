# coding: utf-8
# author: xiaodong
# date  : 2019/11/30


from socket import socket, AF_INET, SOCK_STREAM
import threading


class LazyConnection:
    def __init__(self, address, family=AF_INET, _type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = _type
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, "sock"):
            raise RuntimeError("Already connected!")
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock
