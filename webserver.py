#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options
from urls import handlers
from tinydb import TinyDB

define("port", default=8000)

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            website_title = u"Wargame",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__) + "templates", "static"),
            #xsrf_cookies = True,
            login_url = "/login",
            cookie_secret = "isucsie",
            debug = True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = TinyDB('database.json')

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
