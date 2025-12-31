# File paths

- [[Pathlib module]]
- [[OS module]]
- [[Shelve module]]
- [[Glob Patterns]]

## Current Working Directory ([[CWD]])

- While `folder` is the more **modern name for directory**, note that `current working directory` (or just _`working directory`_) is the standard term, not current working folder

### chdir()

- You can get the current working directory as a string value with the `Path.cwd()` function and can change it using `os.chdir()`
- **There is no pathlib function for changing working directory,** The only way is to use `os.chdir()`

```python
from pathlib import Path
import os

Path.cwd() # cwd = Current Working Directory
# WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python313')'
os.chdir('C:\\Windows\\System32') # change path, remember to escape backslashes on windows
Path.cwd() # check cwd again
# WindowsPath('C:/Windows/System32')
```

### Non-existing directory

- Python will display an **error** if you try to **change** to a **directory** that **does not exist:**

```python
import os
os.chdir('C:/ThisFolderDoesNotExist')

Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
FileNotFoundError: [WinError 2] The system cannot find the file specified:
'C:/ThisFolderDoesNotExist'
```

## Home Directory

* **All users have their own _`Home Directory`_**
* Also called `_home folder_`
* Get `Path` object of home folder by using `Path.home():`

```python
from pathlib import Path
Path.home()
# WindowsPath('C:/Users/Al')
```

* **Location of Home Directories depends on the OS**
	* Windows: `C:\Users`
	* MacOS: `/Users`
	* Linux: `/home`

## Absolute vs Relative Paths

There are 2 ways to specify a filepath

### Absolute Path

* `Absolute Paths` **always start from the root** of the file system (e.g., `C:\`) and uniquely define the location of a file or directory.
* An `absolute path` is the **full address** of a file or directory, starting _**from the root**_.
	* Windows:` C:\`
	* MacOS & Linux: `/`
	
* **Example**: `"C:\Users\Al\Documents\file.txt"` is like a full mailing address.

### Relative Path

* `Relative Path:` is a **partial path**. It's location is **relative to the current working directory**.
* `"Documents\file.txt"` **is like saying "the file in the Documents folder next to you."** It only makes sense if you know where "you" are.
* ***Special* names** that can be used in relative filepath
	* `.` (or implied) refers to the **Current Directory**
	* `..` (dot-dot) indicates **_parent** folder_**, aka **folder above**(one level up)
	* The path `..\..\` moves **two levels up** from the CWD.

## Directory Structure

The **root** of the file system is designated as `C:\`.

* **C:\** (Root Directory)
    * **bacon** (Directory)
        * **fizz** (Directory)
            * `spam.txt` (File)
        * `spam.txt` (File)
    * **eggs** (Directory)
        * `spam.txt` (File)
    * `spam.txt` (File)

### Path Comparison Table

- CWD is **C:\bacon\fizz**. 
- The following table shows **how to reference various files and directories from this position** using both relative and absolute addressing.

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

```python
from pathlib import Path
Path.cwd()  # WindowsPath('F:/Python/Automate boring stuff')
Path.cwd().is_absolute() #True
Path('spam/bacon.eggs').is_absolute() # false
```
## Creating New Folders

To make a directory from a `Path` object call the _`mkdir()`_ method.

### Pathlib

**Example:**
```python
from pathlib import Path
Path(r'C:\\Users\\Al\spam').mkdir() # This will create "spam" folder under home folder
```

### OS module

**Example:**
```python
import os
os.makedris('C:\\delicious\\walnut\\waffles') # will create all those folders if any are missing
```

### Create series of folders and files

- adding an argument `exists_ok=True` doesn't raise error if folder already exists

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

## Checking Drive validity

```python
from pathlib import Path
d_drive = Path('D:/')
m_drive = Path('M:/')

d_drive.exists() # True
m_drive.exists() # False
```

