#!/usr/bin/python3
from sys import argv
from pickle import loads,dumps
if (argv[1] == "refresh"):
	file = open("memory.dat", "wb+")
	file.write(dumps({'B':[]}))
	file.close()
elif (argv[1] == "picture_count"):
	file = open("memory.dat",'rb')
	data = file.read()
	data = loads(data)
	print(len(data[argv[2]]))
