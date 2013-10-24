# -*- coding: utf-8 -*-

import tornado.ioloop
from tornado.options import define, options
import tornado.web

from urls import urls

SETTINGS = dict (
    debug = True
)

application = tornado.web.Application(
                    handlers = urls,
                    **SETTINGS
)

if __name__ == "__main__":
    application.listen(8888)
    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.instance().start()
