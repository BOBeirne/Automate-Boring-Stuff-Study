"""
Identifying Photo Folders on the Hard Drive
I have a bad habit of transferring files from my digital camera to temporary folders somewhere on the hard drive and then forgetting about these folders. 
It would be nice to write a program that could scan the entire hard drive and find these leftover photo folders.

Write a program that goes through every folder on your hard drive and finds potential photo folders. 
Of course, first you’ll have to define what you consider a “photo folder” to be; let’s say that it’s any folder where more than half of the files are photos. 
And how do you define what files are photos? First, a photo file must have the file extension .png or .jpg. 
Also, photos are large images; a photo file’s width and height must both be larger than 500 pixels. 

This is a safe bet, since most digital camera photos are several thousand pixels in width and height.

As a hint, here’s a rough skeleton of what this program might look like:

# Import modules and write comments to describe this program.

for folder_name, subfolders, filenames in os.walk('C:\\'):
	num_photo_files = 0
	num_non_photo_files = 0
	for filename in filenames:
		# Check if the file extension isn't .png or .jpg.
		if TODO:
			num_non_photo_files += 1
			continue  # Skip to the next filename.

		# Open image file using Pillow.

		# Check if the width & height are larger than 500.
		if TODO:
			# Image is large enough to be considered a photo.
			num_photo_files += 1
		else:
			# Image is too small to be a photo.
			num_non_photo_files += 1

	# If more than half of files were photos,
	# print the absolute path of the folder.
	if TODO:
		print(TODO)
When the program runs, it should print the absolute path of any photo folders to the screen.
"""
import os, PIL
from PIL import Image
from pathlib import Path


for folder_name, subfolders, filenames in os.walk('C:\\'):
	num_photo_files = 0
	num_non_photo_files = 0

	for filename in filenames:
		# Check if the file extension isn't .png or .jpg.
		if not (filename.endswith('.png') or filename.endswith('.jpg')): 
			num_non_photo_files += 1
			continue  # Skip to the next filename.
		# Open image

		try:
			src = os.path.join(folder_name, filename)
			img = Image.open(src)
			width, height = img.size
			# Check if the width & height are larger than 500.
			if width >= 500 or height >= 500:
				num_photo_files += 1
			else:
				# Image is too small to be a photo.
				num_non_photo_files += 1
		except PIL.UnidentifiedImageError:
			num_non_photo_files += 1
			continue
		except Exception as err:
			print(f'An exception ocurred {err}')

	total_files = num_photo_files + num_non_photo_files
	if total_files > 0 and (total_files / 2 ) < num_photo_files:
		location = Path.cwd()
		print(f'Potential photo folder {folder_name} ')
