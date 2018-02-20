# TODO
# - logging

from os import env

from .app import create_app


app = create_app(env['WEEWX_DATABASE'])


if __name__ == '__main__':
    app.run(env['DTS_PORT'])
