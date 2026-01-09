"""
script to add logo to corner of each image
1. Load the logo image.
2. Loop over all .png and.jpg files in the working directory.
3. Check whether the image is wider and taller than 300 pixels.
4. If so, reduce the width or height (whichever is larger) to 300 pixels and scale down the other dimension proportionally.
5. Paste the logo image into the corner.
6. Save the altered images to another folder.
"""

import os
from PIL import Image

SQ_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size

os.makedirs('withLogo', exist_ok=True) # we will be saving edited image to new folder

for file in os.listdir('.'): # walk the cwd
	if not (file.endswith('.png') or file.endswith('jpg')) or file == LOGO_FILENAME: #skip anything that we are not editing and logo
		continue

	img = Image.open(file) # open the file
	width, height = img.size # get the size of the image into 2 values

	if width > SQ_FIT_SIZE and height > SQ_FIT_SIZE: # check if file needs resizing
		if width > height:# if the height is an issue
			height = int((SQ_FIT_SIZE / width) * height) # make it SMALLER focusing on height
			width = SQ_FIT_SIZE
		else:
			width = int((SQ_FIT_SIZE / height) *width)
			height = SQ_FIT_SIZE

		print(f' Resizing {file}')
		img = img.resize((width, height)) # resize image, remember to use tuple

	print(f'Adding logo to {file}')
	img.paste(logo_img, (width - logo_width, height - logo_height), logo_img) # calculate logo location and paste it in, logo_img as 3rd arg ensures transparency of logo

	img.save(os.path.join('withLogo', file)) # save new file