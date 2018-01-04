# TODO
# - logging

from sys import argv

from .app import create_app


# TODO args handling
app = create_app(argv[1])
