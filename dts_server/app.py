import json
from json import JSONDecodeError
from traceback import print_exc

import weewx_orm
from flask import Flask, request


def create_app(database, into_='''
    :param database: Name of database to save into
    '''):
    app = Flask(__name__)

    weewx_db = weewx_orm.WeewxDB(database)

    @app.route('/data', methods=['POST'])
    def route_data():
        try:
            data = json.loads(request.stream.read())
            weewx_db.archive_insert_data(data)
        except JSONDecodeError:
            print_exc()
            return 422, 'Invalid JSON'

        except IOError:
            print_exc()
            return 500, 'Unable to save data'
        return ''

    @app.route('/')
    def route_index():
        return 'hello world'

    return app
