1.  What is []?

empty list

2.  How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains `[2, 4, 6, 8, 10]`.)

`spam[2] = 'hello'`

For the following three questions, assume spam contains the list `['a', 'b', 'c', 'd']`.

3.  What does `spam[int(int('3' * 2) // 11)]` evaluate to?

The expression '3' * 2 evaluates to the string '33'. 
`int('33') is 33. 33 // 11` is 3. 
So the expression simplifies to `spam[3]`, which evaluates to 'd'.

4.  What does spam[-1] evaluate to?

'd'

5.  What does spam[:2] evaluate to?

'a' , 'b'

For the following three questions, assume bacon contains the list `[3.14, 'cat', 11, 'cat', True]`.

6.  What does bacon.index('cat') evaluate to?

1

7.  What does bacon.append(99) make the list value in bacon look like?

it will add new entry type `int(99)` at the end of list

8.  What does `bacon.remove('cat')` make the list value in bacon look like?

it will remove first occurrence of str 'cat' and leave the other one while moving all values after removed values one space to earlier

9.  What are the operators for list concatenation and list replication?

`+` and `*`

10.  What is the difference between the `append()` and `insert()` list methods?

`append()` add entry at the end of list and `insert()` needs specified index and inserts the value in the list moving the list entries to make space for it

11.  What are two ways to remove values from a list?

`remove()` and `del list[1]` and `pop()`

12.  Name a few ways that list values are similar to string values.

you can split a string into list of letters
they can be indexed, sliced and used in for loops

13.  What is the difference between lists and tuples?

lists can be modified and tuples cannot
lists use square brackets `[]` and tuples rounded `()`

14.  How do you write the tuple value that has just the integer value 42 in it?

`tuple = (42,)`

15.  How can you get the tuple form of a list value? How can you get the list form of a tuple value?

`new_tuple = tuple(list)`
`new_list = list(tuple)`

16.  Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

references to those variables

17.  What is the difference between `copy.copy()` and `copy.deepcopy()`?

`deepcopy` copies also the values in the embedded lists (lists of lists)
