# String

- A string is a series of characters surrounded by either single or double quotation marks.
- It's how Python handles words, sentences, and other text data.
- Strings are immutable like [[Tuples]]
  - Once a st is created you cannot change it, to modify it you need to make a new str.
- Use the `+` operator to concatenate (combine) strings
- Use the `*` operator to duplicate strings

## ESCAPE characters

* `\'`  -   single quote        ('say hi to bob\' mother)
* `\"`  -   double quote        
* `\t`  -   Tab
* `\n`  -   Newline             ("Hello there\nHow are You?\nI\'m fine.)
* `\\`  -   Backslash           

## RAW string

- Type of a string that makes string literal

```python
print(r'The file path is F:\Python\Automate boring stuff')
```

## MULTILINE strings

```python
'''
Dear Alice,

This is a body of an e-mail.

Kind regards,

Babs
'''
```

## MULTILINE Comment

```python
"""
Multi line comment

can have more than one line

starts with triple quote and end with triple quote
"""
```
## Indexes and slices

WIP

## in and not operators

WIP

## F-STRINGS (after ver 3.6)

``` python
name = 'Al'
age = 40
print(f'My name is {name} and I\'m {age} years old.')
print(f'in 10 years I will be {age+10} years old')
# F-string alternatives (before ver 3.6) 
```

## string INTERPOLATION (using %s)

``` python
name = 'Al'
age = 40
print('My name is %s and I\'m %s years old.' % (name, age))
print('in 10 years I will be %s years old' % (age +10))
```
## .format() METHOD

```python
name = 'Al'
age = 40
print('My name is {} and I\'m {} years old.'.format(name, age))
print('in 10 years I will be {} years old'.format(age +10))
```

### .format method INDEX

``` python
name = 'Al'
age = 40
print('{1} years ago {0} was born and named {0}.'.format(name, age))
```

## `upper()` and `lower()`

``` python
spam = 'Hello world'
spam = spam.upper()
print(spam)

spam = 'Hello world'
spam = spam.lower()
print(spam)
```

## isupper() and islower()

* `isupper()` and `islower()` returns BOOL value

``` python
spam = 'Hello'
spam = spam.lower()
print(spam.islower())
print(spam.isupper())
```
## other "is" methods

* `.isalpha()`      -       True if str has only letter and isn't blank
* `.isalnum()`      -       True if str is only letters and num and isn't blank 
* `.isdecimal()`    -       True if only numbers and not blank
* `.isspace()`      -       True if str consists of only: spaces, tabs and newlines and isn't blank
* `.istitle()`      -       True if all words start with uppercase followed by only lowercases


## .startswith and .endswith

```python
print(('Hello World!').startswith('Hello'))
print(('Hello World!').endswith('World!'))
print(('Hello World!').endswith('!'))
```
## Joining and splitting strings

### JOINING strings

```python
print(', '.join(['cats', 'bats', 'rats'])) # remember we start with list and then turn it into a str!
```

### SPLITTING strings

```python
print('My name is Simon'.split()) #  this turns string into the list
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))

experiment = '''
Dear Alice,
There is a milk bottle in the fridge
that is labelled "Milk Experiment."
Please do not drink it,
Sincerely,
Babs
'''
print(experiment.split('\n'))
```

## Justifying and Centering text 

### rjust() and ljust() methods

```python
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello'.rjust(50))

print('Hello'.ljust(10))
print('Hello'.ljust(50))
```

### using "fill characters"

```python
print('Hello'.rjust(10, '*'))
print('Hello'.ljust(20, '~'))
```
### center() method

```python
print(' Hello '.center(20, '~'))
```

## Removing whitespaces 

### strip()

```python
longline = '            hello              '
print(longline.strip())
```

### lstrip() & rstrip()

```python
longline = '            hello              '
print(longline.lstrip())
longline = '            hello              '
print(longline.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
```

## Numeric Code Points of Characters ([Unicode] code points)

### ord()

```python
print(ord('A'))

print(ord('B'))

print(ord('b'))

print(ord('9'))

print(ord('@'))
```

### chr()

```python
print(chr(22))

print(chr(33))

print(chr(2))

print(chr(65))

print(chr(99))
```

### chr() and ord() mathematic operations

```python
print(chr(ord('A')+1))

print(ord('A') < ord('B'))
```

## more info about strings:

* https://nedbatchelder.com/text/unipain.html  
* https://www.youtube.com/watch?v=MijmeoH9LT4

## copying and pasting strings - see [[Pyperclip module]]
