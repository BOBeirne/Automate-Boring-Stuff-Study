## [[Shutil]]

* Shell Utilities
* can be used to **copy, copy tree, rename and move files**

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
