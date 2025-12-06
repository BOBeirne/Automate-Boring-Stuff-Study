# File paths

[[Pathlib module]]
[[OS module]]
[[Shelve module]]
[[Glob Patterns]]

## Current Working Directory ([[CWD]])

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

Python will display an **error** if you try to **change** to a **directory** that **does not exist:**


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

#### Directory Structure Overview

The root of the file system is designated as `C:\`.

* **C:\** (Root Directory)
    * **bacon** (Directory)
        * **fizz** (Directory)
            * `spam.txt` (File)
        * `spam.txt` (File)
    * **eggs** (Directory)
        * `spam.txt` (File)
    * `spam.txt` (File)

#### Path Comparison Table

The current working directory is **C:\bacon\fizz**. The following table shows how to reference various files and directories from this position using both relative and absolute addressing.

| Current Working Directory (CWD) | Relative Paths | Absolute Paths |
| :---: | :---: | :--- |
| **C:\bacon\fizz** | `..\` | `C:\bacon\` |
| **C:\bacon\fizz** | `.. \` | `C:\` |
| **C:\bacon\fizz** | `.\fizz` | `C:\bacon\fizz` |
| **C:\bacon\fizz** | `.\fizz\spam.txt` | `C:\bacon\fizz\spam.txt` |
| **C:\bacon\fizz** | `..\spam.txt` | `C:\bacon\spam.txt` |
| **C:\bacon\fizz** | `..\..\eggs` | `C:\eggs` |
| **C:\bacon\fizz** | `..\..\eggs\spam.txt` | `C:\eggs\spam.txt` |
| **C:\bacon\fizz** | `..\..\spam.txt` | `C:\spam.txt` |

####  Key Path Facts

* **Absolute Paths** always start from the **root** of the file system (e.g., `C:\`) and uniquely define the location of a file or directory.
* **Relative Paths** are defined **relative to the Current Working Directory (CWD)**.
    * **`.\`** (or implied) refers to the **Current Directory**.
    * **`..\`** refers to the **Parent Directory** (one level up).
    * The path `..\..\` moves **two levels up** from the CWD.

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

#### Create series of folders and files

```python
from pathlib import Path
h = Path.home()
(h / 'spam').mkdir(exist_ok=True)  # exists_ok=True doesn't raise error if folder already exists
(h / 'spam/eggs').mkdir(exist_ok=True)
(h / 'spam/eggs2').mkdir(exist_ok=True)
(h / 'spam/eggs/bacon').mkdir(exist_ok=True)
for f in ['spam/file.txt','spam/eggs/file2.txt', 'spam/eggs/file3.txt', 'spam/eggs/bacon/file4.txt']:
	with open(h / f, 'w', encoding='utf-8') as file: # opening "with" automatically closes file when exists the loop
		file.write('Hello')
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

