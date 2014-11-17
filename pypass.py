#!/usr/bin/python

import os, random

file    = "password.pas"
keyfile = "keyfile.key"

def generateKey(length):
    key = ""
    for i in range(length):
        number = random.randint(0,255)
        key += hex(number)[2:]
    return key

print generateKey(128)


