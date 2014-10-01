#!/usr/bin/python

import tornado.web

handlers = [
    (r"/", "controllers.main.IndexHandler"),
    (r"/rule", "controllers.main.RuleHandler"),
    (r"/challenge", "controllers.main.ChallengeHandler"),
    (r"/signup", "controllers.main.SignUpHandler"),
    (r"/login","controllers.main.LoginHandler"),
    (r"/scoreboard","controllers.main.RankHandler"),
    (r".*", "controllers.main.PageNotFound"),
]
