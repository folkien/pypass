#!/usr/bin/python

import os, random, argparse, time

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputfile", 	type=str, 		 required=True)
parser.add_argument("-c", "--crypt", 	action='store_true', required=False)
parser.add_argument("-d", "--decrypt", 	action='store_true', required=False)
args = parser.parse_args()

random.seed(time.time())

def generateKey(length):
    key = ""
    for i in range(length):
        number = random.randint(0,255)
        key += hex(number)[2:]
    return key

print generateKey(128)

myfile = open(args.inputfile, 'r')
if myfile.is_opened:
		print "ok"
else:
		print "wrong"


