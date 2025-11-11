## Shelve module

Uses **binary** files to store **variables data**

```python
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fuzzball']
shelfFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats'] # ['Zophie', 'Pooka', 'Simon', 'Fuzzball']
```

You can make changes to it as if it were a dictionary

### .keys() & .values()

Returns a list of key values in shelve file

```python
shelfFile = shelve.open('mydata')
shelfFile.keys()
list(shelfFile.keys()) # display the keys as a list

shelfFile.values()
list(shelfFile.values()) # display values as a list
```
