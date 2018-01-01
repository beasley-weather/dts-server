# todo
# - logging

from flask import Flask, request

import weewx_orm


app = Flask(__name__)


@app.route('/data', methods=['POST'])
def route_data():
    data = request.stream.read()
    weewx_orm.archive_insert(data)


def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with Werkzeug Server')
    func()
