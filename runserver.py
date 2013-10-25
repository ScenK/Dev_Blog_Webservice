# -*- coding: utf-8 -*-

import os
import logging

import tornado.ioloop
from tornado.options import define, options
import tornado.web

from urls import urls
from config import SETTINGS

application = tornado.web.Application(
                    handlers = urls,
                    **SETTINGS
)

define("port", default=8888, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    logging.info("Starting Tornado web server on http://127.0.0.1:%s" % options.port)
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
