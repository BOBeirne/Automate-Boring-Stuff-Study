# Write a program that walks through a folder tree and searches for files with a certain file extension 
# (such as .pdf or .jpg). Copy these files from their current location to a new folder.

# import all needed modules
from pathlib import Path
import os, re, shutil

REGEX = re.compile(r'(\.jpg|\.pdf)') # specify REGEX to search for specific file types

source_path = Path.cwd() # specify path to look for .pdf or .jpg in cwd

copy_folder = "pdfs_jpgs_copies" 
dest_path = Path.cwd() / copy_folder # specify path to folder where to copy to

for folder, subfolder, file in os.walk(source_path):
# check if new folder for copies exists and if not create it
	if not dest_path.exists():
		dest_path.mkdir()

for f in file:
	print(f'Checking folder: {folder} ...')
	if re.search(REGEX, f): # check if file matches regex
		print(f'Found match: {f}')
		shutil.copy(Path(folder) / f, dest_path / f)
		
print('Done.')