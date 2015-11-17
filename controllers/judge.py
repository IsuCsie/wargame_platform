#!/usr/bin/python
# -*- coding: utf-8 -*-


class Judger(object):
    w10_key = "ISU{}"
    w50_key = "ISU{}"
    w100_key = "ISU{comment_is_very_important}"
    w200_key = "ISU{jsfuck_is_rock!}"
    w300_key = "ISU{stupid_way2use_hash}"

    def verify(self, key):
        if key == self.w10_key:
            result = ["w10", 10, True]
        elif key == self.w50_key:
            result = ["w50", 50, True]
        elif key == self.w100_key:
            result = ["w100", 100, True]
        elif key == self.w200_key:
            result = ["w200", 200, True]
        elif key == self.w300_key:
            result = ["w300", 300, True]
        else:
            result = ["", 0, False]

        return result
