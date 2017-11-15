# todo
# - logging

from flask import Flask, request

from .ipc_client import IPC_Client

app = Flask(__name__)
ipc_client = IPC_Client('tcp://127.0.0.1:34343')


@app.route('/data', methods=['POST'])
def route_data():
    data = request.stream.read()
    print(data)
    with ipc_client:
        ipc_client.transfer(data)
