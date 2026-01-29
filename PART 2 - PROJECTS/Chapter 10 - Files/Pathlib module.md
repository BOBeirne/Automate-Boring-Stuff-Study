# Pathlib module

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
	print(Path(r'C:\Users\Al', filename))
```

`C:\Users\Al\accounts.txt`
`C:\Users\Al\details.csv`
`C:\Users\Al\invite.docx`

## The Golden Rules for joining paths

* To join path components with the **`/`** operator, **at least one of the items you are joining must be a `Path` object**. 
* These expressions evaluate from left to right (->) , and the / operator can be used on:
	* Path object + string 
	* 2 Path objects 
	* NOT on two strings
* if joining multiple paths - either the first or second leftmost value **must** be a Path object for the entire expression to evaluate to a Path object.

### Joining a `Path` object and a string
```python
# The left side is a Path object, the right is a string 
home_path = Path('C:/Users/Al') 
full_path = home_path / 'spam' 
print(full_path) 
# `C:\Users\Al\spam`
```

### Joining two `Path` objects
```python
# Both sides of the '/' are Path objects 
home_path = Path('C:/Users/Al') 
project_folder = Path('my_project') 
full_path = home_path / project_folder 
print(full_path) 
# `C:\Users\Al\my_project`
```

### Chaining multiple parts

- **operator works from left to right** , so you can chain multiple strings as long as the **very first item** is a `Path` object.

```python
# The expression starts with a Path object, so the rest can be strings 
full_path = Path('C:/Users/Al') / 'project' / 'data' / 'file.txt' 
print(full_path) 
# `C:\Users\Al\project\data\file.txt`
```

### Invalid case of Str / Str

- Python will give you a Traceback error if you try to enter the following:

```python
# This will cause an error because both operands are strings 
bad_path = 'spam' / 'bacon' 
print(bad_path)

Traceback (most recent call last):
File "<python-input-0>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Either the first or second leftmost value **must** be a `Path object` for the entire expression to evaluate to a Path object.

### Path Separators

* Windows paths are using backslash `\`, while MacOS and Linux use forward slash `/`
* `path()` function in `pathlib` handles all OS types
* best practice is to use forward slashes `/` in Python code.

``` python
from pathlib import Path
Path("spam","bacon","eggs")
WindowsPath("spam/bacon/eggs") 
# WindowsPath("spam/bacon/eggs")
str(Path("spam","bacon","eggs")) 
#"spam\\bacon\\eggs"
```

## getting parts of a filepath

* You can **extract** filepath's different paths using several Path obj attributes
* This can be useful in **creating new filepaths based of old ones**
* **Parts** of a **filepath** include:
	* **Anchor** - root folder
	* (Windows ONLY) **Drive** - which is a single letter
	* **Parent** - folder that contains the file
	* **Name** of the file:
		* **Stem** - base name
		* **Suffix** - extension
* Only **Windows** have Drive attribute, MacOs and Linux do not!

```python
from pathlib import Path
p = Path('F:\\Python\\Automate boring stuff\\base.base')
p.anchor 
# 'F:\\'
p.drive 
# 'F:'
p.parent 
# WindowsPath('F:/Python/Automate boring stuff')
p.name 
# 'base.base'
p.stem 
# 'base'
p.suffix
# '.base'
```

### p.parts

* **Splitting up path** by it's separator

```python
from pathlib import Path
p = Path('F:\\Python\\Automate boring stuff\\base.base')
p.parts 
# ('F:\\', 'Python', 'Automate boring stuff', 'base.base')
p.parts[3] 
# 'base.base'
p.parts[0:2] 
# ('F:\\', 'Python')
```

### parents (NOT parent)

* Evaluates ancestor's folders of a Path obj with Int index
* **Parent** is the folder that contains the file

```python
from pathlib import Path
Path.cwd() 
# WindowsPath('F:/Python/Automate boring stuff')
Path.cwd().parents[0] 
# WindowsPath('F:/Python')
Path.cwd().parents[1] 
# WindowsPath('F:/')
```