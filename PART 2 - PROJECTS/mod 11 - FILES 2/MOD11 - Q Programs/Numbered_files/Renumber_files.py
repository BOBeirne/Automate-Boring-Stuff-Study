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
import os, re

source_path = Path.cwd() # specify cwd to be where we will work on the files
gap = None
nrs = []
file_list = []

def find_matching_files(source_path, nrs, file_list):

	regex = re.compile(r'^file+_(\d+).txt$')
	#print(source_path)
	for filename in os.listdir(source_path):
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
    for i in range(len(sorted_nrs) -1):
        #print(i)
        if sorted_nrs[i+1] - sorted_nrs[i] > 1: # if gap between sorted nrs is bigger than 1
            #print(i)
            return sorted_nrs[i] # returns the missing nr
            

find_matching_files(source_path, nrs, file_list)
find_gap(nrs)
#print(find_gap(nrs))



# TODO go through the list of files and find any gaps
# TODO close the gap by renaming all files above the gap