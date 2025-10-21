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

# TODO import all needed modules
from pathlib import Path
import os, re, shutil


# TODO create regex looking for MM and DD
# TODO search all filenames in cwd
# TODO compare names of files to american format standard (MM-DD_YYYY)
# TODO if files are found, swap the MM and DD values respectively by renaming the file