## File

- Files consist of:
	* Filename
	* Filepath
	* Extension

### Root folder (Anchor)

* contains all other folders on that hard drive
* Different for OS  
	* Windows `C:\` , 
	* MacOS & Linux is `/.`
* Additional Volumes (USB Drive/CD etc) will appear differently on different OS
	* Windows: `D:\` or `E:\` etc
	* MacOS : separate folders in `/Volumes` folder
	* Linux: separate folders under `/mnt` folder (mount)


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
