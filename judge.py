#!/usr/bin/python
# -*- coding: utf-8 J-*-

import json
from collections import namedtuple


def readJSON(file_name):
    with open(file_name) as f:
        return json.load(f)

flag_fmt = "ISU{{{}}}"

pairS = namedtuple('pairS', ['subj', 'scor'])

answer_dict = {flag_fmt.format(each['answ']): pairS(each['subj'], each['scor']) for each in readJSON('problems.json')}

class Judger(object):
    def verify(self, key):
        if key in self.answer_dict.keys():
            pairs = self.answer_dict[key]
            result = (pairs.subj, pairs.scor, True)
        else:
            result = ('', 0, False)

        return result
