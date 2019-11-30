# coding: utf-8
# author: xiaodong
# date  : 2019/11/30

from collections import defaultdict
from contextlib import contextmanager

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)


class DisplayMessage:
    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print("msg[{}]: {!r}".format(self.count, msg))


_exchange = defaultdict(Exchange)

def get_exchange(name):
    return _exchange[name]


if __name__ == '__main__':

    exc = get_exchange("just-a-name")
    task_1 = DisplayMessage()
    task_2 = DisplayMessage()
    with exc.subscribe(task_1, task_2):
        exc.send("msg1")
        exc.send("msg2")
