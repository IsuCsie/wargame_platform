#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 給ADR逆向那題打分數用的script

from tinydb import TinyDB, where
import time, datetime
import sys

def R100Scorer(username):
    db = TinyDB('database.json')
    Users = db.table('Users')

    t = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    current = Users.search(where("username") == username)[0]

    Users.update({"r100": t, "score": (current["score"]+100)}, cond=where("username")==username)

if __name__ == "__main__":
    R100Scorer(sys.argv[1])
