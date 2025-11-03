# Copy current working directory path using pyperclip
import pyperclip, os, sys

if len(sys.argv) > 1: # checks for any command line arguments
	os.chdir(sys.argv[1]) # changes the current working directory of the program (every program has it's own cwd)
pyperclip.copy(os.getcwd()) # copies the current working directory

# you don't hve to use pause line in .bat file because there is no print function