# coding: utf-8
# author: xiaodong
# date  : 2019/11/30

from queue import Queue
from threading import Thread, Event


class ActorExit(Exception):
    ...


class Actor(object):

    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print("Got: ", msg)


if __name__ == '__main__':
    p = PrintActor()
    p.start()
    p.send("hello")
    p.send("world")
    p.close()
    p.join()
