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

    def get_current_user(self):
        return self.get_secure_cookie('user')

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
    @tornado.web.authenticated
    def get(self):
        username =  self.get_current_user()
        news = []
        self.render("challenge.html",username=username, news=news)

class RankHandler(BaseHandler):
    @removeslash
    def get(self):
        self.render('scoreboard.html')


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

            if len(username) < 9 or len(password) < 4:
                raise

            if " " in username or " " in password:
                raise

            if Users.search((where("username") == username) | (where("email") == email)):
                raise

            Users.insert({
                "username": username,
                "password": password,
                "email": email
            })
            self.render("signup_success.html")

        except:
            self.render("signup_fail.html")

class LoginHandler(BaseHandler):
    @removeslash
    def get(self):
        self.render("login.html")
    
    def post(self):
        Users = self.db.table('Users')
        username = self.get_argument("username")
        password = md5.new(self.get_argument("password")).hexdigest()
        login = Users.get(where('username') == username)
        if login is not None:
            if login.get('password') == password:
                self.set_secure_cookie("user",self.get_argument("username"))
                self.redirect('/challenge')
        else:
            self.write('login failed ...')
            self.wirte('<meta http-equiv="refresh" content="1;url=/" >')

class PageNotFound(BaseHandler):
    def get(self):
        self.render("404.html")


