#!/usr/bin/python
# -*- coding: utf-8 -*-

class Reverse100Validator(object):
    def decoder(self, plain):
        output = ""
        originString = plain
        strTarget = len(originString) % 3;
        for i in range(0, len(originString)):
            output += chr(ord(originString[i]) - 0x3 - strTarget);
        return output
    
    def encoder(self, password):
        output = ""
        encryptedString = password
        strTarget = len(encryptedString) % 3
        for i in range(0, len(encryptedString)):
            output += chr(ord(encryptedString[i]) + 0x3 + strTarget);
        return output

class Judger(object):
    w100_key = "456"
    w200_key = "789"
    p100_key = "abc"
    f100_key = "def"

    def verify(self, key):
        r100validator = Reverse100Validator().decoder(key)
        if ("USER" in r100validator and
            "BYPASS_1000Limits" in r100validator and
            "TryToFixMemoryList" in r100validator and
            "TryToFixCRC32_ToBYPASS" in r100validator and
            "AbleToInput1000_OnTextBox" in r100validator):
            return ["r100", 100, True]
        else:
            if key == self.w100_key:
                return ["w100", 100, True]
            elif key == self.w200_key:
                return ["w200", 200, True]
            elif key == self.p100_key:
                return ["p100", 100, True]
            elif key == self.f100_key:
                return ["f100", 100, True]
            else:
                return ["", 0, False]
