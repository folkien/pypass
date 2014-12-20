#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, random, argparse, time, sys

data = ""

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputfile", 	type=str, 		 		required=False)
parser.add_argument("-o", "--outputfile", 	type=str, 		 		required=False)
parser.add_argument("-k", "--keyfile", 		type=str, 		 		required=False)
parser.add_argument("-c", "--crypt", 		action='store_true', 	required=False)
parser.add_argument("-n", "--newkey", 		type=int, 				required=False)
args = parser.parse_args()

random.seed(time.time())

def generateKey(length):
    key = []
    for i in range(length):
        key.append(random.randint(0,255))
    return key

def cipher(text,key):
	key_length  = len(key)
	text_length = len(text)
	for i in range(text_length):
			text[i] = chr(ord(text[i]) ^ key[i % key_length] )
	return text

def saveKey(filename,key):
	kfile = open(filename, "w")
	for i in range( len(key) ):
			kfile.write( format(key[i], '02x') )
	kfile.close()

def loadKey(filename):
	kfile = open(filename, "r")
	data = kfile.read()
	kfile.close()
	i = 0
	key = []
	while ( i < len(data) ):
			key.append(int(data[i]+data[i+1],16))
			i += 2
	return key

#tworzymy nowy klucz
if args.newkey:
	key = generateKey(args.newkey)
	saveKey(args.keyfile, key)
	print "Wygenerowano nowy klucz."

#Otwieramy plik do szyfrowania
if args.inputfile:
		if os.path.exists(args.inputfile):
                        if os.access("myfile", os.R_OK):
                            #otwieramy klucz
                            myfile = open(args.inputfile, 'r')
                            data = list(myfile.read())
                            myfile.close()
                        else:
                            sys.exit("Brak dostępu do pliku! Spróbuj wykonać polecenie jako root.")
		else:
			print "File to encryption doesn't exist."
			sys.exit(1)

#Szyfrujemy plik
if args.crypt:
	#Sprawdzamy czy istnieje klucz
	if os.path.exists(args.keyfile):
		#otwieramy klucz
		key = loadKey(args.keyfile)
	else:
		print "Keyfile doesn't exists."
		sys.exit(2)
	#szyfrujemy plik
	data = cipher(data,key)

if args.outputfile:
	#zapisujemy plik
	myfile = open(args.outputfile, 'w')
	myfile.write("".join(data))
	myfile.close()
else:
	#wyswietlamy plik
	sys.stdout.write("".join(data))

