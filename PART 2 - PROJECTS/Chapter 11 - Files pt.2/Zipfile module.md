# [[ZIP]] files

## Creating ZIP file
### ZipFile()

Needs to be imported `import zipfile`
Requires **2 arguments**:
* string or **Path** object
* **'w'** (similar to 'w' in .open() when writing files)
### .write()

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

## Reading ZIP file

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

## Extracting files from ZIP file

### .extractall()

Extracts all contents of ZIP file into current working directory 
It can take optional argument of a Path to extract to

```python
import zipfile
example_zip = zipfile.ZipFile('example.zip')
example_zip.extractall() # you can otpionally provide folder variable here
example_zip.close()
```

### .extract()

Extracts a single, specified file into a cwd
Can also optionally specify path to extract to
If folder doesn't yet exist, Python will create it.

```python
example_zip.extract('file.txt')
example_zip.close()
```