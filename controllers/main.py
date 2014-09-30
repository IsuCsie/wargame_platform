#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
import md5

from tinydb import TinyDB, where
from tornado.web import removeslash

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def abort(self, code):
        raise tornado.web.HTTPError(code)

class IndexHandler(BaseHandler):
    @removeslash
    def get(self):
        self.render("index.html")

class RuleHandler(BaseHandler):
    @removeslash
    def get(self):
        self.render("rule.html")

class ChallengeHandler(BaseHandler):
    @removeslash
    def get(self):
        self.render("challenge.html")

class SignUpHandler(BaseHandler):
    @removeslash
    def get(self):
        self.render("signup.html")

    def post(self):
        try:
            Users = self.db.table('Users')
            username = self.get_argument("username")
            password = self.get_argument("password")
            email = self.get_argument("email")

            password = md5.new(password).hexdigest()

            if self.db.search((where("username") == username) | (where("email") == email)):
                raise

            Users.insert({
                "username": username,
                "password": password,
                "email": email
            })
            self.render("signup_success.html")

        except:
            self.render("signup_fail.html")

class PageNotFound(BaseHandler):
    def get(self):
        self.render("404.html")
