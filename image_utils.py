#!/usr/bin/python3
from PIL import Image
def checkDotsNear(dot, pixels):
	dots = []
	for x in range(-1, 2):
		for y in range(-1, 2):
			if (x == 0 and y == 0):
				continue
			newDot = (dot[0]+x, dot[1]+y)
			if (pixels[newDot] != (255,255,255)):
				dots.append(newDot)
	return dots

def matchShape(corner, pixels):
	checkedDots = []
	dots = checkDotsNear(corner,pixels)
	while (dots != []):
		for i in dots:
			if (pixels[i] != (255,255,255)):
				checkedDots.append(i)
				dots.extend(checkDotsNear(i, pixels))
				pixels[i] = (255,255,255)
			else :
				dots.remove(i)
	return checkedDots
def getLetters(image):
	pixels = image.load()
	c = 0
	letters = []
	while(True):
		corner = []
		for x in range(image.width):
			if (corner != []):
				break
			for y in range(image.height):
				if (pixels[(x,y)] != (255,255,255)):
					corner = [x,y]
					break
		if (corner == []):
			break
		image.putpixel(corner, (0, 255,0))
		dots = matchShape(corner, pixels)
		x = map(lambda x : x[0], dots)
		y = map(lambda x : x[1], dots)
		x = list(x)
		y = list(y)
		letter = Image.new("RGB", (max(x)-min(x)+1, max(y)-min(y)+1), color=(255,255,255))
		for dot in dots:
			letter.putpixel((dot[0]-min(x), dot[1]-min(y)), (0,0,0))
			pixels[dot] = (255,255,255)
		letters.append(letter)
		corner = []
		c += 1
	print(len(letters))
	return letters
