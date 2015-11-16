#!/usr/bin/python
# -*- coding: utf-8 -*-


class Judger(object):
    w100_key = "ISU{comment_is_very_important}"
    w200_key = "ISU{jsfuck_is_rock!}"
    w300_key = "ISU{stupid_way2use_hash}"

    def verify(self, key):
        if key == self.w100_key:
            return ["w100", 100, True]
        elif key == self.w200_key:
            return ["w200", 200, True]
        elif key == self.w300_key:
            return ["w300", 300, True]
        else:
            return ["", 0, False]
