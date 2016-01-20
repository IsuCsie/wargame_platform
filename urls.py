#!/usr/bin/python

handlers = [
    (r"/test", "controllers.main.ChallengeHandler"),
    (r"/", "controllers.main.IndexHandler"),
    (r"/challenge", "controllers.main.ChallengeHandler"),
    (r"/submit", "controllers.main.SubmitHandler"),
    (r"/signup", "controllers.main.SignUpHandler"),
    (r"/login", "controllers.main.LoginHandler"),
    (r"/logout", "controllers.main.LogoutHandler"),
    (r"/scoreboard", "controllers.main.RankHandler"),
    (r".*", "controllers.main.PageNotFound"),
]
