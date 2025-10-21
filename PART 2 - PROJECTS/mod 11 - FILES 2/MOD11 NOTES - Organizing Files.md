# Copy, Move and Delete files
## [[Shutil]]

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


## [[ZIP]] files

### Creating ZIP file
#### ZipFile()

Needs to be imported `import zipfile`
Requires **2 arguments**:
* string or **Path** object
* **'w'** (similar to 'w' in .open() when writing files)
#### .write()

it takes **3 arguments**:
* **Path** argument - path of the file to be compressed and added to ZIP file
* **compress_type** - compression type (which algorithm) to use
	* zipfile.ZIP_DEFLATED - deflation algorithm works well on all types of data
	* if no algorithm is provided it will not compress the file, just add it to ZIP uncompressed
* **compresslevel** - compression level - (Python 3.7+)
	* in range 0-9 with 9 being slowest but providing highest data compression
	* default is lvl 6 . if no arg is specified

```python
import zipfile
def
if

with open('file.txt', 'w', encoding='utf-8') as file_object: # using "with" ensures that file is stored as a variable and is closed after it leave "with" block
	file_object.write('Hello' * 10000)

with zipfile.ZipFile('example.zip', 'w') as example_zip: # store example.zip as variable allowinf to operate on it, ensuring it close()'s after operaton leave with statement's block
	example_zip.write('file1.txt, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
```

### Reading ZIP file

To read contents of a ZIP file you need to first **create ZipFile object** by calling `zipfile.ZipFile()` and pass it ZIP filename

```python
import zipfile
example_zip = zipfile.ZipFile('example.zip')
```

You can use **.namelist()** methods to read the list of files inside the ZIP file

```python
example_zip.namelist() # returns a list of files inside ZIP file like ['file1.txt']
```

* **.getinfo()** - allows to turn the **file inside ZIP** file into variable
* **.filesize()** - gets the original size of the file before ZIPped
* **.compress_size()** - returns size after compression

```python
file1_info = example_zip.getinfo('file1.txt')
file1_info.filesize # returns the size of file in bytes
file1_info.compress_size # returns the size of compressed file in bytes

print(f'Compressed file is {round(file_info.filesize / file1_info.compress_size), 2}x smaller') # calculate the ratio of compressed end result and round it up to .2 decimal spaces

example_zip.close() # if not using "with" you need to remember to close it at the end
```

### Extracting files from ZIP file

#### .extractall()

Extracts all contents of ZIP file into current working directory 
It can take optional argument of a Path to extract to

```python
import zipfile
example_zip = zipfile.ZipFile('example.zip')
example_zip.extractall() # you can otpionally provide folder variable here
example_zip.close()
```

#### .extract()

Extracts a single, specified file into a cwd
Can also optionally specify path to extract to
If folder doesn't yet exist, Python will create it.

```python
example_zip.extract('file.txt')
example_zip.close()
```