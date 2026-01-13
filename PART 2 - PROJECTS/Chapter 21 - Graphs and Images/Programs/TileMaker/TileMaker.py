"""
Write a program that produces a tiled image from a single image, much like tiles of cat faces in Figure 21-6. 
Your program should have a make_tile() function with three arguments: 
a string of the image filename, 
an integer for how many times it should be tiled horizontally, 
and an integer for how many times it should be tiled vertically. 

The make_tile() function should return a larger Image object of the tiled image.
You will use the paste() methods as part of this function.

For example, 
if zophie_the_cat.jpg was a 20×50-pixel image, calling make_tile('zophie_the_cat.jpg', 6, 10) should return a 120×500 image with 60 tiles total. 
For a bonus, try randomly flipping or rotating the image to tile when pasting it to the larger image. 
This tile maker works best with smaller images to tile. 
See what abstract art you can create with this code.
"""
import sys
from PIL import Image
import random

imgFilename = sys.argv[1]
horizontalTileNo = int(sys.argv[2])
verticalTileNo = int(sys.argv[3])


def make_tile(file, horizontal, vertical):
	img = Image.open(file)
	width, height = img.size # get width and height of the original to calculate final size
	tiledImgWidth = width * horizontal
	tiledImgHeight = height * vertical
	tiledImg = Image.new('RGBA', (tiledImgWidth, tiledImgHeight))

	for y in range(vertical): # loop through y axis
		for x in range(horizontal): # loop through x axis
			left = x * width # calculate left coordinate
			top = y * height # calculate top coordinate
			imgCopy = img.copy() # work on copy

			# Random rotate
			randomRotate = [0, 90, 180, 270]
			choice = random.choice(randomRotate)
			#print(f'rotating {choice} degrees' ) # test
			imgCopy = imgCopy.rotate(choice, expand=True) # update the value

			# Random flip 
			randomFlip = ['horizontal', 'vertical', 'none']
			choice = random.choice(randomFlip)
			if choice == 'horizontal':
				#print('Flipping horizontally') # test
				imgCopy == imgCopy.transpose(Image.FLIP_LEFT_RIGHT)  # update the value
			elif choice == 'vertical':
				#print('Flipping vertically') # test
				imgCopy = imgCopy.transpose(Image.FLIP_TOP_BOTTOM)  # update the value
			else:
				pass
			#print(f'pasting new tile at x: {x} x y: {y}') # print coordinates # test
			tiledImg.paste(imgCopy, (left, top)) # paste
	
	# Save and show the result
	tiledImg.save('tiled_'+ file)
	tiledImg.show()

# Check the commandline arguments
if len(sys.argv) == 4: # 1 program name, 2 filename, 3 horizontal tile no and 4 vertical tile no
	try:
		print(f'Processing {imgFilename} for tile size {horizontalTileNo} x {verticalTileNo} tiles')
		make_tile(imgFilename, horizontalTileNo, verticalTileNo)
	except Exception as err:
		print(f'Exception: {err}')
else:
	print('Provide: 3 arguments: n\1) filename with extension, \n2) number of horizontal tiles and \n3) number of vertical tiles \nas 3 arguments when running the program')
	sys.exit()
