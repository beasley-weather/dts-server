# TODO
# - logging

from sys import argv

from .app import create_app


# TODO args handling
if len(argv) != 2:
    raise Exception('Missing arguments: database')

app = create_app(argv[1])

if __name__ == '__main__':
    # TODO add port argument
    app.run()
