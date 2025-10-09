
# Simple [list]

```python
spam = ['cat', 'dog', 'bat']
print('Original list:' , spam)
```
# .append()

```python
spam.append('moose') add arg at the end of list
print('after appending moose:' ,spam)
```
# .insert()

```python
spam.insert(1, 'chicken') # insert chicken at index[1]
print('after inserting chicken', spam)
```
# .remove()

```python
spam.remove('bat') # removes 1st instance of a specified value
print('after removing bat:', spam)
```
# .sort()

```python
bacon = [1, 5, 6, 2, 0, 3.14, 22, -9]
bacon.sort()
print('after sorting', bacon)

spam.sort() #also works on strings but not on combination!!!
print('sorting strings', spam)
```

# .sort() reversed

```python
spam.sort(reverse=True)
print('using reverse sorting', spam)
```
# Sort ASCIIbetical 

* uppercase comes first then lowercase
* 
```python
egg = ['cat', 'dog', 'Bat', 'Chicken', 'Zebra']
egg.sort()
print('sorting ASCIIbetically', egg)
```
# .reverse() 

```python
egg.reverse()
print('simply using.reverse method', egg)
```