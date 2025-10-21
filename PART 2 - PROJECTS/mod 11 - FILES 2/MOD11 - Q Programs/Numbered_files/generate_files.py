# this program will generate numbered files with random file removed in the middle to create a gap

import os, random
from pathlib import Path

source_path = Path.cwd()
num_files = 20
random_nr = random.randint(2,19)
generated_files = []

def create_files():
    for i in range(1, num_files + 1):
        filename = f'file_{i}.txt' # create files with numbers
        generated_files.append(filename) # add to list of files to randomly delete from
        with open(filename, "w") as file:
            file.write(f'This is an example file.')        
        # print(f'created {filename} in {source_path}.')
    
        

def delete_rand_file(generated_files):
    file_to_del = random.choice(generated_files)
    os.remove(file_to_del)
    print(f'file {file_to_del} deleted')


create_files()

delete_rand_file(generated_files)
# print(generated_files) # prints list of files to delete

