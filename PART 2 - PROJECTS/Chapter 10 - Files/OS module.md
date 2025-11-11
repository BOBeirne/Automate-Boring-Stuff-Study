# OS module (the old way)
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
