from flask import Flask, request

import weewx_orm


def create_app(database):
    '''
    :param database: Name of database to save into
    '''
    app = Flask(__name__)

    weewx_db = weewx_orm.WeewxDB(database)

    @app.route('/data', methods=['POST'])
    def route_data():
        data = request.stream.read()
        weewx_db.archive_insert_data(data)
        return ''

    @app.route('/')
    def route_index():
        return 'hello world'

    return app
