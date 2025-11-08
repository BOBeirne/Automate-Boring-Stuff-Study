from typing import Union

# 1. Creating an empty dictionary:
```python
empty_dictionary =  {}
```

# 2. Dictionary with type hints: 

* By adding the type hint, you are telling Pylance what to expect.
* dict[str, Union[int, str]] means: "A dictionary with string keys,
* and values that can be either an integer OR a string."

```python
dictionary: dict[str, Union[int, str]] = {'foo': 42} 
dictionary = { 'foo' : 42} 
```

# 3. Difference between a dictionary and list: 

* dictionary item is a collection of key and value `pairs('name':'Zophie)` and list is a collection of single values ('cat')
* lists are ordered while dictionaries are not, you access list using the index `(mylist[0])` and dict is accessed by `key(mydict['name])`

# 4. Accessing a non-existent key:

* I will get error if value is not present unless i use call where i assign default val to 0
  
```print('I have ' +str(dictionary.get('money', 0)) + '$ in my bank account')```

# 5. in spam.keys() vs in spam: 

* `spam.keys()` only checks they key values while "in spam()" checks whole dictionary

# 6. Checking for values:

* `spam.values()` in spam only checks for values in dictionary

# 7. Setting a default value:
* `setdefault()` method for eg. 
* ```dictionary.setdefault('job', 'lawyer')```

# 8. Using the * operator on a dictionary:
* star syntax "unpacks" the keys
  ```print(*dictionary)```