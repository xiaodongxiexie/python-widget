import stomp


class MQ_Producer(stomp.StompConnection10):
    def __init__(self, host_and_ports=[("localhost", 61613)],
                       username='admin', passwd='admin'):
        super(MQ_Producer, self).__init__(reconnect_attempts_max=100000)
        self.conn = stomp.Connection10(host_and_ports)
        self.conn.connect(username, passwd)

    def sendmsg(self, name, msg, content_type=None, headers=None, **kw):
        self.conn.send(name, msg, content_type=content_type, headers=headers, **kw)

    def stop(self):
        self.conn.stop()


if __name__ == '__main__':

    name = 'just-for-test'
    Producer = MQ_Producer()
    for i in range(10):
        Producer.sendmsg(name, "{}".format(i))
    while True:pass