#!/usr/bin/python3
from sys import argv
from time import time
from pickle import dumps,loads
from utils import OpenMemoryAndImage
images, memory = OpenMemoryAndImage(argv)
starttime = time()
if (len(argv) == 3):
	image = images[0]
	letter = argv[2]
	pixels = []
	print(letter)
	print("Training mode")
	for x in range(image.width):
		for y in range(image.height) :
			pixels.append(int(image.getpixel((x,y)) == (255,255,255)))
	if (letter in memory.keys()):
		memory[letter].append(pixels)
	else :
		memory[letter] = [pixels,]
	memoryFile = open("memory.dat", "wb+")
	memoryFile.write(dumps(memory))
	memoryFile.close()
else :
	s = ''
	print(len(images))
	for image in images:
		print("Practic mode")
		equality = 0
		letter = ''
		max_percent = 0
		for i in memory.keys():
			print ('Trying letter ' + i)
			allpixels = memory[i]
			for picture in allpixels :
				pos = 0
				for x in range(image.width):
					for y in range(image.height) :
						try :
							if (picture[pos] == int(image.getpixel((x,y))==(255,255,255))):
								equality += 1
						except :
							pass
						pos += 1
				percent = equality/(image.width*image.height)
				if (percent > max_percent):
					max_percent = percent
					letter = i
				equality = 0
		print("It is", letter)
		s+=letter
print(s, time()-starttime)
