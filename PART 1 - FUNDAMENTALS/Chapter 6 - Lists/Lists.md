
# List

- Can be also called an `array` in **other programming languages**
- A **value**, which contains **multiple other values** in an **ordered sequence**
- Lists are **mutable** (can have values changed, added and removed)
- Uses **square brackets, witch commas separating each item** `[1,2,3,4]`
- You can initialize an **empty list** by simply using 2 square brackets `emptyList = []` 
- You can get items out of list by calling it's **index number**
  - Index **starts from 0** (so 1st position is list[0], 2nd is list[1] and so on..)


**Example** of a simple list:

```python
spam = ['cat', 'dog', 'bat']
print('Original list:' , spam)
```
## .append()

```python
spam.append('moose') # add arg at the end of list
print('after appending moose:' ,spam)
```
## .insert()

```python
spam.insert(1, 'chicken') # insert chicken at index[1]
print('after inserting chicken', spam)
```
## .remove()

```python
spam.remove('bat') # removes 1st instance of a specified value
print('after removing bat:', spam)
```
## .sort()

```python
bacon = [1, 5, 6, 2, 0, 3.14, 22, -9]
bacon.sort()
print('after sorting', bacon)

spam.sort() #also works on strings but not on combination!!!
print('sorting strings', spam)
```

## .sort() reversed

```python
spam.sort(reverse=True)
print('using reverse sorting', spam)
```
## Sort ASCIIbetical 

* uppercase comes first then lowercase
* 
```python
egg = ['cat', 'dog', 'Bat', 'Chicken', 'Zebra']
egg.sort()
print('sorting ASCIIbetically', egg)
```
## .reverse() 

```python
egg.reverse()
print('simply using.reverse method', egg)
```