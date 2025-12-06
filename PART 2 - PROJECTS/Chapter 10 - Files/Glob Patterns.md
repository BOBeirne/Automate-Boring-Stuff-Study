## Glob patterns

* You can use *`*`* and *`?`* to match folder names and filenames
* called glob patterns aka simplified [[Regex module]]
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