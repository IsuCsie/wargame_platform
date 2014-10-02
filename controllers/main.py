#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
import md5
import time, datetime

from judge import Judger
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
    check_result = False
    @removeslash
    @tornado.web.authenticated
    def get(self):
        username =  self.get_current_user()
        self.render("challenge.html",username=username, check_result=self.check_result)

    @tornado.web.authenticated
    def post(self):
        username = self.get_current_user()
        key = self.get_argument("key")
        result = Judger().verify(key)
        self.check_result = result[2]
        if self.check_result is True:
            Users = self.db.table('Users')
            user = Users.search(where("username") == username)[0]
            current_score = user["score"]
            score = current_score + result[1]
            problem = result[0]
            t = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            Users.update({"score": score, problem: t}, cond=where("username")==username)
            self.render("challenge.html", username=username, check_result=self.check_result)
        else:
            self.render("challenge.html", username=username, check_result=self.check_result)

class RankHandler(BaseHandler):
    def sortByScore(self, element):
        return element["score"]

    @removeslash
    def get(self):
        Users = self.db.table('Users')
        records = sorted(Users.all(), key=self.sortByScore, reverse=True)
        self.render('scoreboard.html', records=records)

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
                "email": email,
                "score": 0,
                "r100": "",
                "w100": "",
                "w200": "",
                "p100": "",
                "f100": ""
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
            self.write('<meta http-equiv="refresh" content="1;url=/" >')

class LogoutHandler(BaseHandler):
    @removeslash
    def get(self):
        self.clear_cookie("user")
        self.redirect('/')

class PageNotFound(BaseHandler):
    def get(self):
        self.render("404.html")


