# Write a program that opens all .txt files in a folder 
# and searches for any line that matches a user-supplied regular expression, then prints the results to the screen.

import re #for regex search
from pathlib import Path # for file operations

current_folder = Path('.')
pattern = input('Input a regex: ')
REGEX = re.compile(pattern)

for file in current_folder.glob('*.txt'):
    file_contents = file.read_text() #open each file to see the text
    lines = file_contents.splitlines() # split whole string into lines
    for line in lines: # search each line
        if REGEX.search(line): # if there is a match
            print(line) # print it
print('Search complete.')