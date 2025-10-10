## Files and File paths

### File

* **Filename**
* **Filepath**
* **Extension**
### Filepath

#### Root folder (Anchor)

* contains all other folders on that hard drive
* Different for OS  
	* Windows `C:\` , 
	* MacOS & Linux is `/.`
* Additional Volumes (USB Drive/CD etc) will appear differently on different OS
	* Windows: `D:\` or `E:\` etc
	* MacOS : separate folders in `/Volumes` folder
	* Linux: separate folders under `/mnt` folder (mount)

#### Path Separators

* Windows paths are using backslash `\`, while MacOS and Linux use forward slash `/`
* `path()` function in `pathlib` handles all OS types
* best practice is to use forward slashes `/` in Python code.

``` python
from pathlib import Path
Path("spam","bacon","eggs)
WindowsPath("spam/bacon/eggs") # WindowsPath("spam/bacon/eggs")
str(Path("spam","bacon","eggs)) #"spam\\bacon\\eggs"
```

#### Parts of a filepath

* You can extract filepath's different paths using several Path obj attributes
* This can be useful in creating new filepaths based of old ones
* **Parts** of a **filepath** include:
	* **Anchor** - root folder
	* (Windows) **Drive** - which is a single letter
	* **Parent** - folder that contains the file
	* **Name** of the file:
		* **Stem** - base name
		* **Suffix** - extension
* Only **Windows** have Drive attribute, MacOs and Linux do not!

```python
from pathlib import Path
p = Path('F:\\Python\\Automate boring stuff\\base.base')
p.anchor # 'F:\\'
p.drive # 'F:'
p.parent # WindowsPath('F:/Python/Automate boring stuff')
p.name # 'base.base'
p.stem # # 'base'
p.suffix # 'base'
```

#### p.parts

* Splitting up path by it's separator

```python
from pathlib import Path
p = Path('F:\\Python\\Automate boring stuff\\base.base')
p.parts # ('F:\\', 'Python', 'Automate boring stuff', 'base.base')
p.parts[3] # 'base.base'
p.parts[0:2] # ('F:\\', 'Python')
```

#### parents (NOT parent)

* Evaluates ancestor's folders of a Path obj with Int index*

```python
from pathlib import Path
Path.cwd() # WindowsPath('F:/Python/Automate boring stuff')
Path.cwd().parents[0] # WindowsPath('F:/Python')
Path.cwd().parents[1] # WindowsPath('F:/')
Path.cwd().parents[2]
```

## OS module (old way)
### path.join()

* it takes a bunch of str arguments and returns them as a single path
* the result will be different for different OS

```python
import os
os.path.join('folder1','folder2','folder3','file.png')
```

* Windows: `'folder1\\folder2\\folder3\\file.png`
* Linux or Mac: `'folder1/folder2/folder3/file.png`
### .sep()

value for .join() function is stored in os.sep module (separator)

```python
os.sep
```

* Windows: `'\\'`
* Linux or Mac: `'/'`

### .getcwd()

returns **C**urrent **W**orking **D**irectory

```python
os.getcwd() # 'F:\\Python\\Automate boring stuff'
```

### .chdir()

* **changes** the Current Working Directory (**cwd**)
* use it by providing a new path to change to

```python
os.chdir('C:\\')
os.getcwd() # 'C:\\'
```

### path.abspath()

* returns **absolute path to** a specified folder or file

```python
os.path.abspath('base.base') # 'F:\\Python\\Automate boring stuff\\base.base'
os.path.abspath('..\\..\\base.base') #'F:\\base.base'
```

### path.isabspath()

a way to establish **if** a passed **path is absolute or not**
returns either **True or False**

```python
os.path.isabspath('F:\\Python\\Automate boring stuff\\base.base') #True
os.path.isabspath('\\Folder3\\base.base') #False
```
### path.relpath()

Returns a **relative path** from starting point

```python
os.path.relpath('C:\\folder1\\folder2\\file.text','C:\\folder1') # 'folder2\\file.text'
```

### path.dirname()

Returns a **directory part of a path**

```python
os.path.dirname('F:\\Python\\Automate boring stuff\\base.base') # 'F:\\Python\\Automate boring stuff'
```
### path.basename()

Returns only the **last item in the path**

```python
os.path.basename('F:\\Python\\Automate boring stuff\\base.base') # 'base.base'
```

### path.exists()

**Checks** if the file actually **exists**
Returns either **True or False**

```python
os.path.exists('F:\\Python\\Automate boring stuff\\base.base') # True
```

### path.isfile() & path.isfolder()

Checks if the file is indeed a **file** or **folder**
Returns either **True or False**

```python
os.path.isfile('F:\\Python\\Automate boring stuff\\base.base') # True
os.path.isfolder('F:\\Python\\Automate boring stuff\\base.base') # False
```

### path.getsize()

Returns **size in bytes** of the folder or file provided

```python
os.path.getsize('F:\\Python\\Automate boring stuff\\base.base')  # 39
```

### os.listdir()

```python
os.listdir('F:\\Python')  # ['Automate boring stuff', 'Nanny app idea.txt', 'NSA python training.url', 'p1i8awsivji51.jpg', 'Programs', 'Projects']
```

### .makedirs()
You can create new folders with **_os.makedirs()_** function
It accepts both relative or absolute paths

```python
import os
os.makedirs('C:\\delicious\\walnut\\waffles') # and it does make the folders...
```
## Pathlib module

* use `from pathlib import Path` otherwise you have to enter *pathlib.Path()* everywhere 
* **Object-Oriented:** It treats paths as objects, not just strings. This is its biggest advantage. It means you can call methods directly on the path object, leading to cleaner and more readable code.
* `WindowsPath` representation uses forward slashes `/` due to developers preference for Linux.
	* if passed as a str() it will show path with double backslashes as to escape the backslash
	* for MacOS or Linux this is opposite. 
* For Mac/Linux `Path()` would return `PosixPath` object
	* _POSIX_ is a set of standards for Unix-like operating systems.
* **There is no pathlib function for changing working directory, You MUST use os.chdir()**

```python
from pathlib import Path
my_files = 'accounts.txt', 'details.csv', 'invite.docx'
for filename in my_files:
	print(Path(r'C:\\Users\\Al', filename))
```

C:\Users\Al\accounts.txt
C:\Users\Al\details.csv
C:\Users\Al\invite.docx
### The Golden Rule for joining paths

* To join path components with the **`/`** operator, **at least one of the items you are joining must be a `Path` object**. 
* These expressions evaluate from left to right (->) , and the / operator can be used on:
	* Path object + string 
	* 2 Path objects 
	* NOT on two strings
	
*  Example 1: **Joining a `Path` object and a string**

```python
# The left side is a Path object, the right is a string 
home_path = Path('C:/Users/Al') 
full_path = home_path / 'spam' 
print(full_path) # `C:\Users\Al\spam`
```

* Example 2: **Joining two `Path` objects**

```python
# Both sides of the '/' are Path objects 
home_path = Path('C:/Users/Al') 
project_folder = Path('my_project') 
full_path = home_path / project_folder 
print(full_path) # `C:\Users\Al\my_project`
```

* Example 3: ***Chaining multiple parts**
	* The operator works from left to right, so you can chain multiple strings as long as the very first item is a `Path` object.

```python
# The expression starts with a Path object, so the rest can be strings 
full_path = Path('C:/Users/Al') / 'project' / 'data' / 'file.txt' 
print(full_path) # `C:\Users\Al\project\data\file.txt`
```

* Example: 4: **Invalid case of Str / Str**
	* Python will give you a Traceback error if you try to enter the following:
	
```python
# This will cause an error because both operands are strings 
bad_path = 'spam' / 'bacon' 
print(bad_path)

Traceback (most recent call last):
File "<python-input-0>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Either the first or second leftmost value **_must_** be a Path object for the entire expression to evaluate to a Path object.

## Current Working Directory (CWD)

While _folder_ is the more modern name for directory, note that current working directory (or just _working directory_) is the standard term, not current working folder
You can get the current working directory as a string value with the `Path.cwd()` function and can change it using `os.chdir()`

```python
from pathlib import Path
import os

Path.cwd() # cwd = Current Working Directory
# WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python313')'
os.chdir('C:\\Windows\\System32') # remember to escape backslashes
Path.cwd()
# WindowsPath('C:/Windows/System32')
```

Python will display an error if you try to change to a directory that does not exist:

```python
import os
os.chdir('C:/ThisFolderDoesNotExist')

Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
FileNotFoundError: [WinError 2] The system cannot find the file specified:
'C:/ThisFolderDoesNotExist'
```

**There is no pathlib function for changing working directory,** 
**You MUST use os.chdir()**

## Home Directory

* All users have their own _Home Directory_
* Also called _home folder_
* Get `Path` object of home folder by using `Path.home():`

```python
from pathlib import Path
Path.home()
# WindowsPath('C:/Users/Al')
```

* Location of **Home** Directories depends on the OS
	* Windows: **C:\Users**
	* MacOS: **/Users**
	* Linux: **/home**

## Absolute vs Relative Paths

There are 2 ways to specify a filepath
### Absolute Path
* An _absolute path_ is the full address of a file or directory, starting _from the root_.
	* Windows: C:\
	* MacOS & Linux: /
	
* Example:  "C:\Users\Al\Documents\file.txt" is like a full mailing address.
### Relative Path
* **Relative Path:** A relative path is a partial path. It's location is relative to the current working directory.
* "Documents\file.txt" is like saying "the file in the Documents folder next to you." It only makes sense if you know where "you" are.
* *Special* names that can be used in relative filepath
	* **_._** (dot) indicates **_current** folder_
	* **_.._** (dot-dot) indicates **_parent** folder_

![[Pasted image 20251007124502.png]]

```python
from pathlib import Path
Path.cwd()  # WindowsPath('F:/Python/Automate boring stuff')
Path.cwd().is_absolute() #True
Path('spam/bacon.eggs').is_absolute() # false
```
## Creating New Folders

To make a directory from a `Path` object call the _mkdir()_ method.

This code will create "spam" folder under home folder

```python
from pathlib import Path
Path(r'C:\\Users\\Al\spam').mkdir()
```

Os version

```python
import os
os.makedris('C:\\delicious\\walnut\\waffles') # will create all those folders if any are missing
```
## File Size and Timestamps

### stat() method

* returns **stat_result object** with file size and timestamp
* **st_size** - size in bytes 
	* `divide int by 1024` to get KB
	* `divide int by 1024 ** 2` to get MB
	* `divide int by 1024 ** 3` to get GB
* **st_mtime** - last modified timestamp
* **st_ctime** - creation timestamp 
	* Windows - when file was created
	* Linux / MacOS - when was last time metadata was changed
* **st_atime** - last accessed timestamp (last read)

_**!!!** keep in mind those timestamps can be manually changed and don't have to be accurate_

```python
from pathlib import Path
calc_file = Path('C:/Windows/System32/calc.exe')
calc_file.stat # os.stat_result(st_mode=33279, st_ino=1407374884140869, st_dev=11721261359060020347, st_nlink=2, st_uid=0, st_gid=0, st_size=27648, st_atime=1744746955, st_mtime=1575709787, st_ctime=1575709787)
calc_file.stat().st_mtime # 1575709787.475222

import time
time.asctime(time.localtime(calc_file_stat().st_mtime)) # 'Sat Dec  7 09:09:47 2019'
```

## Glob patterns

* You can use *`*`* and *`?`* to match folder names and filenames
* called glob patterns aka simplified regex
* **`*`** matches any text
* **`?`** matches exactly one char

### Examples of Glob patterns:

*  `'*.txt'` - match all files ending with .txt
* `'project?.txt'` -  will match 'project1.txt', 'projectx.txt' etc
* `'*project.*'` - will match 'carproject.txt', 'secret_project.docx' etc
* `'*'` - will match all filenames
### glob()

Path objects have glob() method for listing any contents in folder that matches Glob pattern
glob() returns generator object (beyond scope of the book) that you'll need to pass to list() to easily view in interactive shell

```python
from pathlib import Path
p = Path('C:/Users/Al/Desktop/Python excersises') # Forwardslashes!!!
p.glob('*') # <map object at 0x00000206A76EABC0>
list(p.glob('*')) # [WindowsPath('C:/Users/Al/Desktop/Python excersises/1.py'), WindowsPath('C:/Users/Al/Desktop/Python excersises/2.py'), WindowsPath('C:/Users/Al/Desktop/Python excersises/test.py')]
```

it can also be used in a loop

```python
from pathlib import Path
for name in Path('C:/Users/Al/Desktop/Python excersises').glob('*'):
	print(name) 
	
"""
C:\Users\Al\Desktop\Python excersises\1.py
C:\Users\Al\Desktop\Python excersises\2.py
C:\Users\Al\Desktop\Python excersises\test.py
"""
```

## Checking Path validity

To avoid potential crashes if provided with non-existing path you can check them first
* **p.exists()** - returns True if path exists and False if it doesn't
* **p.is_file()** - returns True if it is a file and False if it isn't
* **p.is_dir()** -  returns True if it is a directory and False if it itsn't

```python
from pathlib import Path
win_dir = Path('C:/Windows')
non_exist_dir = Path('F:/This/Path/Doesnt/Exist')
cal_file = Path('C:/Windows/System32/calc.exe')

win_dir.exists() # True
non_exist_dir.exists() # False
calc_file.is_file() # True
calc_file.is_dir() # False
```

You can check if drive is mounted by using following code:
```python
from pathlib import Path
d_drive = Path('D:/')
m_drive = Path('M:/')

d_drive.exists() # True
m_drive.exists() # False
```

## Reading & Writing files

### File types
* Plaintext - contain only basic text characters. do not include font size colour etc. Examples: .txt, .py, .md. can be open in simple text editor and read as ordinary str value
* Binary files - all other types such as word processing documents, PDFs, image files, spreadsheets and executables. if you open it in text editor it will look like scrambled nonsense.

### read_text()

returns whole document as a string

```python
from pathlib import Path
p = Path('spam.txt')
p.write_text('Hello, world!') # 13 - indicated 13 chars were written to the file
p.read_text() # 'Hello, world!'
```

#### open() read() write() and close() are more common way to edit text files in python

## Opening Files

### open()

To use the function pass it a str path to the file you want to open
It accepts absolute and relative paths
open() function **returns File object** - simply another type of value
	read-only access, but you can specify it using `'r'`

```python
from pathlib import Path
spam_file = open(Path('spam.txt'), encoding='UTF-8')
```

#### Windows uses cp1252 (extended ASCII) as default so you need to specify...

## Reading plaintext Files

### read()

Allows to read the entire contents (think of it like large str value) of the file

```python
spam_content = spam_file.read()
spam_content # 'Hello, world!'
```

### readlines()

Use it to get a list of strings values from file
```python
from pathlib import Path
sonnet_file = open(Path('sonnet.txt'), encoding='UTF-8')
sonnet_file.readlines() # ["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,']   
```

### write()

It will re-write the existing file and start from scratch

```python
from pathlib import Path
sonnet_file = open(Path('sonnet.txt'), encoding='UTF-8', 'w')
sonnet_file.write('Hellooooo!!!!!!')

```

If file does not exist, python will create it
### append()

It will add new info to the file without removing the previous data

```python
from pathlib import Path
sonnet_file = open(Path('sonnet.txt'), encoding='UTF-8', 'w')
sonnet_file.append('Hellooooo!!!!!!')
```

### close()

Use it to close the file after you read or write it
```python
sonnet_file.close()
```

It is important to release system resources
and to flush buffer after writing to the file
f
## Shelve module

Uses **binary** files to store **variables data**

```python
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fuzzball']
shelfFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats'] # ['Zophie', 'Pooka', 'Simon', 'Fuzzball']
```

You can make changes to it as if it were a dictionary

### .keys() & .values()

Returns a list of key values in shelve file

```python
shelfFile = shelve.open('mydata')
shelfFile.keys()
list(shelfFile.keys()) # display the keys as a list

shelfFile.values()
list(shelfFile.values()) # display values as a list
```
