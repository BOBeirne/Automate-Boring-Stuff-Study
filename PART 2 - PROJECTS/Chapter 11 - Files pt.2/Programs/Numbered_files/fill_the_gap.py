"""
Write a program that 
1. finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on... 
2. in a single folder 
3. and locates any gaps in the numbering (such as if there is a spam001.txt and a spam003.txt but no spam002.txt). 
4. Have the program rename all the later files to close this gap.

To create these example files (skipping spam042.txt, spam086.txt, and spam103.txt), run the following code:

```python
for i in range(1, 121):
	if i not in (42, 86, 103):
		with open(f'spam{str(i).zfill(3)}.txt', 'w') as filename:
			pass
```
"""

# Import all needed modules
from pathlib import Path
import os, re, shutil

# specify cwd to be where we will work on the files
source_path = Path.cwd()
project_folder = ('PART 2 - PROJECTS/mod 11 - FILES 2/MOD11 - Q Programs/Numbered_files')
project_path = source_path / project_folder
os.chdir(project_path) 
#print(project_path)


nrs = []
file_list = []
sorted_nrs = []
regex = re.compile(r'^file+_(\d+).txt$')

def find_matching_files(project_path, nrs, file_list, regex):
	#print(source_path)
	for filename in os.listdir(project_path):
		match = re.search(regex, filename)
		if match: # check if filename matches regex
			#print(f'Found match: {filename}')
			file_list.append(filename)
			nrs.append(int(match.group(1)))

	#print(file_list)
	#print(nrs)
	return file_list, nrs


def find_gap(nrs):
	sorted_nrs = sorted(nrs) # sort the nrs from the list of nrs
	#print(sorted_nrs)
	for i in range(len(sorted_nrs) -1 ):
		#print(i)
		if sorted_nrs[i+1] - sorted_nrs[i] > 1: # if gap between nrs is bigger than 1
			#print(sorted_nrs[i+1])
			return sorted_nrs[i] + 1 # returns the missing nr



def files_to_rename(file_list, gap, regex): # make a list of files to change
	files_to_rename = []
	try:
		for filename in file_list:
		#print(filename)
			match = regex.search(filename)
			if match:
					number = match.group(1)
					if int(number) > gap:
						files_to_rename.append(filename)
	except: # if nothing found, let me know!
		print('No gaps found')
	#print(files_to_rename)
	return files_to_rename

def rename_files(files_to_rename_list, regex): # rename the files above the gap to one less
	files_to_rename_list.sort()
	#print(f'{files_to_rename_list}')
	for filename in files_to_rename_list:
		match = regex.search(filename)
		if match:
			number = int(match.group(1))
			new_nr = number - 1
			new_filename = (f'file_{str(new_nr)}.txt')
			shutil.move(filename, new_filename)
			print(f'renamed {filename} to {new_filename}')
	print('Done.')

find_matching_files(project_path, nrs, file_list, regex)
gap = find_gap(nrs)
print(f'The missing nr is: {gap}')
files_to_rename_list = files_to_rename(file_list, gap, regex)
rename_files(files_to_rename_list, regex)