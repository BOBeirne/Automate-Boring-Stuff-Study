# Copy, Move and Delete files

##  **Permanently** Deleting Files and Folders

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

If passed a path to list method it will list all **folders, subfolders and files** in one long string.

For easier readability pass it root folder in the for loop and it will walk the whole folder tree in that root folder:

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

```

You can use the **os.walk()** function on tree of folders and rename each file to uppercase letters:

```python
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
It will return a **list**

```python
import os
os.listdir(r'C:\Users\Al')
```

### iterdir()

You can also get a list of **WindowsPath** objects in a folder by calling the iterdir() method:

```python
from pathlib import Path
home = Path.home() # C:\users\usrname
list(home.iterdir())
```


