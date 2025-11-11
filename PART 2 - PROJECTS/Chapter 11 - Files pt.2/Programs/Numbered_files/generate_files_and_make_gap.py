# this program will generate numbered files with random file removed in the middle to create a gap

import os, random
from pathlib import Path


num_files = 20
random_nr = random.randint(2,19)
generated_files = []

# specify cwd to be where we will work on the files
source_path = Path.cwd()
project_folder = ('PART 2 - PROJECTS/mod 11 - FILES 2/MOD11 - Q Programs/Numbered_files')
project_path = source_path / project_folder
os.chdir(project_path) 
#print(project_path)

def create_files():
	for i in range(1, num_files + 1):
		filename = f'file_{i}.txt' # create files with numbers
		generated_files.append(filename) # add to list of files to randomly delete from
		with open(filename, "w") as file:
			file.write(f'This is an example file.')        
	print(f'created {filename} in {source_path}.')



def delete_rand_file(generated_files):
	eligible_files = generated_files[1:-1] # makes sure the first and last files are not included in the random choice for deletion
	file_to_del = random.choice(eligible_files)
	os.remove(file_to_del)
	print(f'{file_to_del} deleted')


create_files()

delete_rand_file(generated_files)
# print(generated_files) # prints list of files
