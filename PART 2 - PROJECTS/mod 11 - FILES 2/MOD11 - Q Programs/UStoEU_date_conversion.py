"""
Say your boss emails you thousands of files with American-style dates (MM-DD-YYYY) in their names 
and needs them renamed to European-style dates (DD-MM-YYYY). 
This boring task could take all day to do by hand! Instead, write a program that does the following:

1. Searches all filenames in the current working directory and all subdirectories for American-style dates. 
Use the os.walk() function to go through the subfolders.

2. Uses regular expressions to identify filenames with the MM-DD-YYYY pattern in them—for example, spam12-31-1900.txt. 
Assume the months and days always use two digits, and that files with non-date matches don’t exist. 
(You won’t find files named something like 99-99-9999.txt.)

3. When a filename is found, renames the file with the month and day swapped to make it European-style. 
Use the shutil.move() function to do the renaming.
"""

# import all needed modules
import os, re, shutil

regex = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)') # 3 groups, day-month-year
file_list = []
files_to_rename = []
project_path = input('Please Specify the directory to analyze: ')
if not os.path.exists(project_path):
	print('Invalid directory')
	exit()
print(f'Selected folder to analyze: {project_path}')


# find files matching the format
def find_matching_files(path):
	for filename, subfolder, files in os.walk(path):
		for file in files:
			match = re.search(regex, file)
			if match:
				file_list.append(file)
	#print(file_list)
	return file_list

# check if format is US or EU or not sure
def determine_date_format(filename, regex):
	match = re.search(regex, filename)
	month = int(match.group(1))
	day = int(match.group(2))
	year = int(match.group(3))
	if 1 <= month <= 12 and 1 <= day <= 31 and 2000 <= year <= 2030:
		return "US" # matches US format
	elif 1 <= day <=12 and 1 <= month <= 31 and 2000 <= year <= 2030:
		return "EU" # Matches EU format
	else:
		return "Inconclusive" # does not match with 100% confidence

file_list = find_matching_files(project_path)

#compare files in a list with US format
if file_list:
	for file in file_list:
		date_format = determine_date_format(file, regex)
		if date_format == "US":
			print(f'Found US formatting in file: {file}')
			files_to_rename.append(file)
		elif date_format == "EU":
			print(f'File {file} has already EU formatting')
		else:
			print(f'{file} has inconclusive date, requires further investigation.')
else:
	print('No matches found in the selected directory.')


def rename_files(files_to_rename):
	for filename in files_to_rename:
		match = re.search(regex, filename)
		if match:
			new_filename = f'{match.group(2)}-{match.group(1)}-{match.group(3)}.txt'
			old_path = os.path.join(project_path, filename)
			new_path = os.path.join(project_path, new_filename)
			#shutil.move(old_path, new_path) # dry run first
			print(f'renamed {filename} to {new_filename}')
		else:
			print(f'Error processing the file.')

rename_files(files_to_rename)