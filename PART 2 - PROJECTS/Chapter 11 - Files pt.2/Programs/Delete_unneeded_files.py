# It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. 
# If you’re trying to free up room on your computer, it’s more effective to identify the largest unneeded files first.

# Write a program that walks through a folder tree and searches for exceptionally large files or folders
# say, ones that have a file size of more than 100MB. (Remember that, to get a file’s size, you can use os.path.getsize() from the os module.) 
# Print these files with their absolute path to the screen.

# TODO import all needed modules
import os


# TODO specify the cwd to be where we will search for the big files
project_path = input('Please Specify the directory to analyze: ')
if not os.path.exists(project_path):
	print('Invalid directory')
	exit()
print(f'Selected folder to analyze: {project_path}')

file_list = []

# check all the files and compare their size to >= 100MB 
def find_large_files(project_path):
	for foldername, subfolders, files in os.walk(project_path):
		for file in files:
			full_path = os.path.join(foldername, file)
			file_size_B = os.path.getsize(full_path)
			file_size_KB = file_size_B / 1024
			file_size_MB = round(file_size_KB / 1024, 5)
			#print(f'{file} size: {file_size_MB} MB')
			if file_size_MB >= 100: 
				#print(f'{file} size: {file_size_MB} MB, this is a large file')
				file_list.append(full_path)
	#print(file_list)
	return file_list

# Delete large files
def delete_large_files(file_list):
	for file in file_list:
		try:
			#os.remove(file)
			print(f'{file} has been "deleted".') # Dry run!
		except OSError as errormsg:
			print(f'Error deleting file {file}, {errormsg}')

find_large_files(project_path)
if file_list:
	delete_large_files(file_list)
else: 
	print('No large files found to be deleted in the selected directory.')