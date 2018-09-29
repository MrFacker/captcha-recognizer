from PIL import Image
from pickle import loads
from numpy import array
from image_utils import getLetters

def error (msg):
	print(msg)
	quit()

def readFile (fileName) :
	file = open(fileName, 'rb')
	data = file.read()
	file.close()
	return data

def OpenMemoryAndImage (argv) :
	try :
		image = Image.open(argv[1])
	except Exception as err:
		error(argv[1] +":"+err.strerror)
	try :
		memory = readFile("memory.dat")
	except :
		error("There is no memory !!!")
	try :
		memory = loads(memory)
	except :
		error("Invalid memory format !!!")
	try :
		image = image.convert("RGB")
	except :
		error("Cant convert image to RGB !!!")
#	try :
	images = getLetters(image)
	#except:
	#	error("Cant split image !!!")
	try :
		for i in range(len(images)):
			images[i] = images[i].resize((10,10))
	except :
		error("Cant resize image !!!")
	return images, memory
