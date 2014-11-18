#!/usr/bin/python
import os, random, argparse, time, sys

#Key is generated from below chars.
letters     = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'x', 'y', 'z', 'q', 'w', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'Y', 'X', 'Z', 'Q', 'W']
numbers     = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
signs       = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '[', ']', ';', ':', '<', '>', '?', '.', ',' ]

keys_dir 	= "/home/spasz/python/pypass/keys/"
key_length	= 4096 
key_signs       = letters + numbers + signs


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputfile", 	type=str, 		 required=True)
parser.add_argument("-c", "--crypt", 	action='store_true', required=False)
parser.add_argument("-d", "--decrypt", 	action='store_true', required=False)
parser.add_argument("-n", "--newkey", 	action='store_true', required=False)
args = parser.parse_args()

random.seed(time.time())

def generateKey(length):
    key = []
    for i in range(length):
        key.append( key_signs[ random.randint(0,len(key_signs)-1) ] )
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
if args.newkey:
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
