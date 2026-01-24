# Set

- Set is an unordered collection of unique values
- In Python, you can create a set by passing a **list** to the `set()` function


**example:**
```python
List_WithDuplicates = ['cat', 'dog', 'dog', 'cat', 'bat']
Set_unique = set(List_WithDuplicates) # changes list to a set
print(Set_unique)
#{'bat', 'cat', 'dog'}
```

## Set operations

```python
set1 = {'cat', 'dog', 'mouse', 'bird'}
set2 = {'dog', 'bird', 'fish', 'lizard'}
```

### The & operator finds the items that are in both sets

```python
common_items = set1 & set2
print(f"Common items: {common_items}")
# Output: Common items: {'bird', 'dog'}
```