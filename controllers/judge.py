#!/usr/bin/python
# -*- coding: utf-8 J-*-

import json


def readJSON(file_name):
    with open(file_name) as f:
        return json.load(f)

flag_fmt = "ISU{{{}}}"


class Judger(object):

    answer_dict = {flag_fmt.format(each['answ']): (each['subj'], each['scor']) for each in readJSON('problems.json')}

    def verify(self, key):
        if key in self.answer_dict.keys():
            res = self.answer_dict[key]
            result = (res[0], res[1], True)
        else:
            result = ('', 0, False)

        return result
