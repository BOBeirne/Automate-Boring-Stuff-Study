# It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. 
# If you’re trying to free up room on your computer, it’s more effective to identify the largest unneeded files first.

# Write a program that walks through a folder tree and searches for exceptionally large files or folders
# say, ones that have a file size of more than 100MB. (Remember that, to get a file’s size, you can use os.path.getsize() from the os module.) 
# Print these files with their absolute path to the screen.

# TODO import all needed modules
from pathlib import Path
import os, re, shutil


# TODO import all needed modules
# TODO specify the cwd to be where we will search for the big files
# TODO check all the files and compare their size to >= 100MB 
    # TODO if files size are matching print files with their abs paths