
import time
import datetime

from threading import Lock

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder="./")

socketio = SocketIO(app)

thread = None
lock = Lock()


@app.route("/")
def index():
    return render_template("index.html")#, async_mode=socketio.async_mode)


# @socketio.on("client_event")
# def client_msg(msg):
#   emit("server_response", {"data": msg["data"]})


# @socketio.on("connect_event")
# def connected_msg(msg):
#   emit("server_response", {"data": msg["data"]})


def background_thread():
    count = 0
    while True:
        socketio.sleep(5)
        count += 1
        dt = datetime.datetime.now()
        dt = str(dt)
        socketio.emit("server_response",  {"data": dt})

@socketio.on("connect")
def connect():
    global thread
    with lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8910, debug=True)
