from flask import Flask, request


app = Flask(__name__)


@app.route('/data', methods=['POST'])
def route_data():
    return str(request.stream.read())
