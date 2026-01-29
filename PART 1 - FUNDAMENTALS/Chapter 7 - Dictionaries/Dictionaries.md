# Dictionaries 

- In other programming languages `Dictionary` can be called as `mapping`, `hash map`, `hash table` or `associative array` (because they associate piece of data to another)
- Like a list but stores **key-value pairs**, instead of an ordered sequence. The collection of data is **unordered**
- Dictionaries use curly brackets, you can initialise an empty dictionary with `DictionaryName = {}`
- To access the data inside, unlike index in [[Lists]], is accessed by `key` name.
  - for example: `DictionaryName['key']`
  - `MyCats = {'name': 'Zophie', 'species': 'cat', 'age': 8}`
  - `MyCats['age']` returns `8`
- Think of it **like real Dictionary**. You **think of a word (key) and look it up to get the meaning (value)**


## Example of a simple [dictionary]

``` python
spam = {'color' :  'red', 'age': 42}
```
## Print dictionary

``` python
print(spam)
```
## Basic print with .values .keys and .items:

``` python
print(spam.values())
print(spam.keys())
print(spam.items())
```
# Printing using loops
## loop for values:

```python
for v in spam.values():
    print(v)
```
## loop for keys:

```python
for k in spam.keys():
    print(k)
```
## loop for items:

```python
for i in spam.items():
    print(i)
```
## Using .list() 

```python
print(list(spam.keys()))
```
## IN and NOT IN operators

```python
print('color' in spam )
print('color' not in spam )

print('age' in spam.keys())
print('age' not in spam.keys())
```
## Incorporating Dictionary into string

```python
for k, v in spam.items():
    print('key: ' +str(k) + ', value: ' +str(v))
```
## Use get() method to check if key is present in the dictionary

```python
print('My hair color is ' +str(spam.get('color', 0)))
print('I am ' +str(spam.get('age', 0)) + ' years old')
print('I have ' +str(spam.get('money', 0)) + '$ in my bank account') # not present so it prints as 0$
```
#### its beneficial to use ,get() method instead of simply printing value as otherwise program will crash!!!

## setdefault() method

* 1st arg is key to check for and 
* 2nd arg is val to set to if key doesn't exist
```python
spam.setdefault('job', 'lawyer')
print(spam)
```
## * Star syntax 

* unpacks the *dictionary values without formatting
```python
print(*spam.values())
```
## [Pylance] errors

* By adding the type hint, you are telling Pylance what to expect.
* dict[str, Union[int, str]] 
* means: "A dictionary with string keys, and values that can be either an integer OR a string."
``` python
from typing import Union
dictionary: dict[str, Union[int, str]] = {'foo': 42} # This line will NOT cause an error, because a string is allowed!
dictionary.setdefault('job', 'lawyer')
print(dictionary)
```

## Merging dictionaries 

* There are a few very common ways to "add" or merge two dictionaries. 
* As of Python 3.9, the cleanest way is to use the** | (pipe)** operator:
```python
dict_a = {'name': 'Alice', 'color': 'blue'}
dict_b = {'color': 'red', 'food': 'tacos'}
merged = dict_a | dict_b
print(f"Merged dictionary: {merged}")
```
