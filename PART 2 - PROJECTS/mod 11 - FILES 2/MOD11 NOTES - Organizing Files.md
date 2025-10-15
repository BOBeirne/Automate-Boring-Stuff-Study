# Copy, Move and Delete files
## Shutil

* Shell Utilities

### .copy()

You can use it to **copy and rename** files at the same time
* If destination is a filename, it will be used as the new name of the copied file. 
* If destination is a folder, the file will be copied to that folder with its original name.

```python
import shutil
shutil.copy('c:\\spam.txt', 'c:\\delicious') # copies single file to the specified folder
shutil.copy('c:\\spam.txt', 'c:\\delicious\spamspamspam.txt') #  copies and renames file

# Can also save relative path as a variable
from pathlib import Path
h = Path.home()
shutil.copy(h / 'spam/file1.txt', h) # copy file from C:\Users\Al\spam\file1.txt to home folder
shutil.copy(h / 'spam/file1.txt', h / 'spam/file2.txt') # same as above but changes the name of the copied file to "file2.txt"
```
### .copytree()

Allows for copying full folder **tree**

```python
import shutil
shutil.copy('c:\\delicious', 'c:\\delicious_backup') # copies full folders and subfolders + files under into the new folder

# using relative path as variable 
from pathlib import Path
h = Path.home()
shutil.copytree(h / 'spam', h / 'spam_backup')
```
### .move()

You can use it to **move and rename** files at the same time
Calling **shutil.move(source, destination)** will move the file or folder at the path source to the path destination

```python
import shutil
shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut') # moves the specified file over to the new location

# using relative path as variable
from pathlib import Path
h = Path.home()
(h / 'spam2').mkdir()
shutil.move(h / 'spam/file1.txt', h / 'spam2')
```

#### Rename

You can use .move() method to **rename the files**
If the destination path is **not an existing folder**, shutil.move() will use this path to rename the file.

```python
import shutil
shutil.move('c:\\delicious\\walnut\spam.txt', 'c:\\delicious\\walnut\spamspamspam.txt') #  Renames the file


# using relative path as variable
from pathlib import Path
h = Path.home()
shutil.move(h / 'spam/file1.txt', h / 'spam2/new_name.txt')
```

## #### **Permanently** Deleting Files and Folders

#### Dry Run

Before running operations that actually delete files it's a good idea to run a dry run, where you:
* comment out # deleting file line
* print(filename) of the deleted file

```python
import os

os.chdir('C:\\Users\testuser\Desktop')
for filename in os.listdir():
	if filename.endswith('.txt'):
		#os.unlink(filename) - this would delete the file
		print(f'{filename} to be deleted') #  pretends to delete the file to confirm what actually gets deleted
```

### unlink()

Permanently deletes a **single file**

```python
import os
os.getwd() # get current path to understand where are we using relative path 
os.unlink('spam.txt') # permanently delete the file
```

### rmdir()

Permanently delete **empty** folder

```python
import os
os.rmdir('')
```

### shutil.rmtree()

Remove folder, subfolders and files inside

```python
import shutil
shutil.rmtree('C:\\Delicious')
```

## Deleting to the Recycle Bin
### send2trash

Just send files and folders passed to **recycling bin**
Needs to be installed via pip

```python
import send2trash
send2trash.send2trash('C:\\Users\testuser\Desktop\IMPORTANT_FILE.txt')
```

## Walking a Directory Tree

### os.walk()

Pass it root folder and it will walk the whole folder tree in that root folder

```python
import os

for folderName, subfolders, filenames in os.walk('C:\\delicious')
	print('The folder is:' + folderName)
	print('The subfolders in ' + folderName + ' are ' + str(subfolders))
	print('The filenames in ' + folderName + ' are ' + str(filenames))
	print()
	
	
	for subfolder in subfolders:
		if 'fish' in subfolder: # if subfolder name contains "fish"
			#os.rmdir(subfolder) # delete the subfolder (after dry run)
			print('rmdir on ' + subfolder) # remember to Dry Run first!

	for file in filenames:
		if file.endswith('.py'): # find all python files
			shutil.copy(os.join(folderName, file), os.join(folderName, file) + '.backup') # and rename them as backup


# ------------------------------------------------------------------------------------------------------------------------------------
# Use the os.walk() function on tree of folders and rename each file to uppercase letters:

from pathlib import Path
h = Path.home()

for folder_name, subfolders, filenames in os.walk(h / 'spam'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': '+ filename)
        # Rename file to uppercase:
        p = Path(folder_name)
        shutil.move(p / filename, p / filename.upper())
   
    print('')
```
### os.listdir()

Pass it a folder name to list all files and subfolders in a specified folder

```python
import os
os.listdir
```


### interdir()

You can also get a list of Path objects in a folder by calling the iterdir() method: