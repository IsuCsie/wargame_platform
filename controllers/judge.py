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
    w100_key = "dd6241867c5965b76c64e47345a97464"
    w200_key = "fb17114d6c3a0d5040779bad5cad38f0"
    p100_key = "{key_is_ISU_CSIE_Buffer_Overflow}"
    f100_key = "3xt u|\|del3te r0c|<5!"

    def verify(self, key):
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
