#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
import md5
import time
import datetime

from judge import Judger, readJSON
from tinydb import where
from tornado.web import removeslash

challenge_list = "problems.json"


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


class ChallengeHandler(BaseHandler):
    @removeslash
    def get(self):
        all_challenges = readJSON(challenge_list)
        ifHint = readJSON('config.json')['ifHint']
        self.render("challenge.html", challenges=all_challenges, isHint=ifHint)


class SubmitHandler(BaseHandler):
    check_result = False

    @removeslash
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        self.render("submit.html", username=username,
                    check_result=self.check_result)

    @tornado.web.authenticated
    def post(self):
        username = self.get_current_user()
        key = self.get_argument("key")
        result = Judger().verify(key)
        self.check_result = result[-1]
        Users = self.db.table('Users')
        user = Users.search(where("username") == username)[0]
        if self.check_result is True and user[result[0]] == "":
            current_score = user["score"]
            score = current_score + result[1]
            problem = result[0]
            t = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            Users.update({"score": score, problem: t, "lastSubmit": t},
                         cond=where("username") == username)

        self.render("submit.html", username=username, check_result=self.check_result)


class RankHandler(BaseHandler):
    @removeslash
    def get(self):
        Users = self.db.table('Users')
        records = sorted(Users.all(), key=lambda element: element['lastSubmit'], reverse=False)
        records = sorted(records, key=lambda element: element['score'], reverse=True)
        challenges = [each['subj'] for each in readJSON(challenge_list)]
        self.render('scoreboard.html', records=records, challenges=challenges)


class SignUpHandler(BaseHandler):
    @removeslash
    def get(self):
        self.render("signup.html")

    def post(self):
        try:
            Users = self.db.table('Users')
            username = self.get_argument("username")
            password = self.get_argument("password")

            password = md5.new(password).hexdigest()

            if len(username) < 9 or len(password) < 4:
                raise

            if " " in username or " " in password:
                raise

            if Users.search((where("username") == username)):
                raise

            person_info = {each['subj']: '' for each in readJSON(challenge_list)}

            person_info.update(username=username,
                               password=password,
                               lastSubmit='',
                               score=0)

            Users.insert(person_info)

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

        if login is not None and login.get('password') == password:
            self.set_secure_cookie("user", self.get_argument("username"))
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
