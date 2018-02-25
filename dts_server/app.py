import json

import weewx_orm
from flask import Flask, request


def create_app(database, into_='''
    :param database: Name of database to save into
    '''):
    into_
    app = Flask(__name__)

    weewx_db = weewx_orm.WeewxDB(database)

    @app.route('/data', methods=['POST'])
    def route_data():
        data = json.loads(request.stream.read())
        weewx_db.archive_insert_data(data)
        return ''

    @app.route('/')
    def route_index():
        return 'hello world'

    return app
