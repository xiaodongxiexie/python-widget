import stomp

content = [1, 2, 3, 4]

class MQ_Consumer(stomp.ConnectionListener):
    def __init__(self, host_and_ports=[('localhost', 61613)],
                       username="admin", passwd="admin"):
        self.conn = stomp.Connection10(host_and_ports, reconnect_attempts_max=100000)
        self.conn.set_listener("SampleListener", self)
        self.conn.connect(username, passwd)
        self.flag = True
        self.dict = {}

    def on_error(self, headers, message):
        self.flag = False

    def on_message(self, headers, message):
        for msg in content:
            url = "http://xxxx.xxxx.xxxx" + str(msg)
            print(url, message)
        self.dict = {}
        message_id = headers['message-id']
        self.conn.ack(message_id)

    def receivemsg(self, queue_name):
        self.conn.subscribe(queue_name, ack="client-individual")

    def stop(self):
        self.conn.stop()

if __name__ == '__main__':
    name = 'just-for-test'
    Consumer = MQ_Consumer()
    Consumer.receivemsg(name)
    while True:pass
