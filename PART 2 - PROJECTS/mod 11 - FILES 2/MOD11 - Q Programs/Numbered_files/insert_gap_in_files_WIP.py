# Write program that can insert gaps into numbered files 
# and bump up the nrs in the filenames after the gap, so that a new file can be inserted.
# ----------------------------

# import all needed modules
import os, shutil, re, random
from pathlib import Path

# specify cwd to be where we will work on the files
source_path = Path.cwd()
project_folder = ('PART 2 - PROJECTS/mod 11 - FILES 2/MOD11 - Q Programs/Numbered_files')
project_path = source_path / project_folder
os.chdir(project_path) 
#print(project_path)

regex = re.compile(r'^file+_(\d+).txt$')
nrs = []
file_list = []

def find_matching_files(project_path, nrs, file_list, regex):
	#print(source_path)
	for filename in os.listdir(project_path):
		match = re.search(regex, filename)
		if match: # check for filenames matching regex
			#print(f'Found match: {filename}')
			file_list.append(filename) # make a list of files to choose from
			nrs.append(int(match.group(1))) # make a separate list of numbers to choose from
	#print(file_list)
	#print(nrs)
	return file_list, nrs

def choose_rand_file(file_list):
	eligible_files = file_list[1:-1] # makes sure the first and last files are not included in the random choice
	#print(eligible_files)
	rand_file = random.choice(eligible_files)
	#print(rand_file)
	#print(f'{rand_file} has been chosen to become a gap')
	return rand_file

def rename_files(file_list, rand_file, regex): # rename the files gap and above for + 1
	file_list = sorted(file_list) # TODO figure out a way to sort using numbers only
	#print(f'{file_list}')
	rand_file_id = file_list.index(rand_file)
	for filename in file_list[rand_file_id:-1]:
		match = regex.search(filename)
		if match:
			number = int(match.group(1))
			new_nr = number + 1
			new_filename = (f'file_{str(new_nr)}.txt')
			shutil.move(filename, new_filename)
			print(f'renamed {filename} to {new_filename}')

file_list, nrs = find_matching_files(project_path, nrs, file_list, regex)
if len(file_list) >= 3:
	#print(file_list)
	rand_file = choose_rand_file(file_list)
	print(rand_file)
	rename_files(file_list, rand_file, regex)
else:
	print('not enough files to insert a gap (min. 3 files)')

# TODO stuck on how to figure out a way to sort using numbers only