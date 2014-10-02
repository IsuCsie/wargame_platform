#!/usr/bin/python
# -*- coding: utf-8 -*-

class Judger(object):
    r100_key = "123"
    w100_key = "456"
    w200_key = "789"
    p100_key = "abc"
    f100_key = "def"

    def verify(self, key):
        if key == self.r100_key:
            return ["r100", 100, True]
        elif key == self.w100_key:
            return ["w100", 100, True]
        elif key == self.w200_key:
            return ["w200", 200, True]
        elif key == self.p100_key:
            return ["p100", 100, True]
        elif key == self.f100_key:
            return ["f100", 100, True]
        else:
            return ["", 0, False]
