#!/usr/bin/python
import os, random, argparse, time, sys

keys_dir 	= "/home/spaszko/python/pypass/keys/"
key_length	= 4096

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

def cipher(text,key):
	key_length  = len(key)
	text_length = len(text)
	for i in range(text_length):
			text[i] = chr(ord(text[i]) ^ ord(key[i % key_length]))
	return text


try:
	myfile = open(args.inputfile, 'r')
except:
	print "This file doesn't exist."
	sys.exit(0)


data = list(myfile.read())

#Sprawdzamy czy istnieje klucz
if os.path.exists(keys_dir + args.inputfile + ".key"):
	keyfile = open( keys_dir + args.inputfile + ".key", "r")
	key = list(keyfile.read())
	keyfile.close()
	#Odszyfrowujemy plik
	data = cipher(data,key)

#wyswietlamy plik
sys.stdout.write("".join(data))

#tworzymy nowy klucz
key = generateKey(key_length)
keyfile = open( keys_dir + args.inputfile + ".key", "w")
keyfile.write("".join(key))
keyfile.close()

#szyfrujemy ponownie
data = cipher(data,key)

#zapisujemy plik
myfile = open(args.inputfile, 'w')
myfile.write("".join(data))
myfile.close()
