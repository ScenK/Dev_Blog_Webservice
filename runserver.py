"""."""
import logging

import tornado.web
from tornado.ioloop import IOLoop
from tornado.options import define, options

from config import SETTINGS
from ws.urls import urls

application = tornado.web.Application(
    handlers=urls,
    **SETTINGS
)

define("port", default=8888, help="run on the given port", type=int)

if __name__ == "__main__":
    options.parse_command_line()
    logging.info(
        f"Starting Tornado web server on http://127.0.0.1:{options.port}")
    application.listen(options.port)
    IOLoop.instance().start()
