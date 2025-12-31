# File

- **Files** consist of:
	* **Filename**
	* **Filepath**
	* **Extension**

## File types

* **Plaintext** - contain only basic text characters. do not include font size colour etc. Examples: .txt, .py, .md. can be open in simple text editor and read as ordinary str value
* **Binary** files - all other types such as word processing documents, PDFs, image files, spreadsheets and executables. if you open it in text editor it will look like scrambled nonsense.

# Root folder (Anchor)

* **Contains all other folders on that hard drive**
* Different for OS  
	* **Windows** `C:\` , 
	* **MacOS** & **Linux** is `/.`
* **Additional Volumes** (USB Drive/CD etc) will appear differently on different OS
	* **Windows**: `D:\` or `E:\` etc
	* **MacOS** : separate **folders** in `/Volumes` folder
	* **Linux**: separate **folders** under `/mnt` folder (mount)


# Reading & Writing files

## read_text()

returns **whole document as a string**

```python
from pathlib import Path
p = Path('spam.txt') # specify a file name and hold it in p variable
p.write_text('Hello, world!') # write content into the file
# 13 - indicated 13 chars were written to the file
p.read_text() # read contents of file
# 'Hello, world!'
```

## open() read() write() and close() 

- Those are more **common** way to edit text files in python

### open()

- To use the `open()` function **pass it a str path to the file you want to open**
- It **accepts absolute and relative paths**
- `open() function` **returns `File object`** 
- **read-only access by default**, but you can specify it using `'r'`
- **Windows uses** cp1252 (extended **ASCII**) **as default** so you need to **specify encoding**

```python
from pathlib import Path
spam_file = open(Path('spam.txt'), encoding='UTF-8') 
```

## read()

- Plaintext only
- Allows to read the entire contents (think of it like large str value) of the file

```python
spam_content = spam_file.read()
spam_content 
# 'Hello, world!'
```

## readlines()

- Use it to **get a list of strings values from file**

```python
from pathlib import Path
sonnet_file = open(Path('sonnet.txt'), encoding='UTF-8')
sonnet_file.readlines() 
# ["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,']   
```

## write()

- It will **overwrite** the existing file and start from scratch
- **If file does not exist, python will create it**
- 
```python
from pathlib import Path
sonnet_file = open(Path('sonnet.txt'), encoding='UTF-8', 'w')
sonnet_file.write('Hellooooo!!!!!!')
```

## append()

- It will **add new info to the file without overwriting the previous data**

```python
from pathlib import Path
sonnet_file = open(Path('sonnet.txt'), encoding='UTF-8', 'w')
sonnet_file.append('Hellooooo!!!!!!')
```

### close()

- Use it to **close the file after you read or write it** 
  - to release memory resources
  - prevent data loss
  - and to flush buffer after writing to the file

```python
sonnet_file.close()
```

# File Size and Timestamps

## stat() method

- keep in mind **those timestamps can be manually changed** and don't have to be accurate_

* returns **stat_result object** with file size and timestamp
* **st_size** - size in bytes 
	* `divide int by 1024` to get KB
	* `divide int by 1024 ** 2` to get MB
	* `divide int by 1024 ** 3` to get GB
* **st_mtime** - last modified timestamp
* **st_ctime** - creation timestamp 
	* **Windows** - **when** file was **created**
	* **Linux** / **MacOS** - when was **last time** metadata was **changed**
* **st_atime** - last accessed timestamp (last read)


```python
from pathlib import Path
calc_file = Path('C:/Windows/System32/calc.exe')
calc_file.stat # os.stat_result(st_mode=33279, st_ino=1407374884140869, st_dev=11721261359060020347, st_nlink=2, st_uid=0, st_gid=0, st_size=27648, st_atime=1744746955, st_mtime=1575709787, st_ctime=1575709787)
calc_file.stat().st_mtime # 1575709787.475222

import time
time.asctime(time.localtime(calc_file_stat().st_mtime)) # 'Sat Dec  7 09:09:47 2019'
```