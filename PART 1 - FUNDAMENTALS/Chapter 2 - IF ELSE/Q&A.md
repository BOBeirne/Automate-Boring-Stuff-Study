# IF & ELSE loops

## 1. What are the two values of the Boolean data type? How do you write them?

True and False

## 2. What are the three Boolean operators?

AND NOT OR 

## 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
```python
AND

1 AND 1 = 1
1 AND 0 = 0
0 AND 1 = 0
0 AND 0 = 0

NOT 1 = 0
NOT 0 = 1

OR
1 OR 1 = 1
1 OR 0 = 1
0 OR 1 = 1
0 OR 0 = 0
```
## 4. What do the following expressions evaluate to?

```
print((5 > 4) and ( 3 == 5)) # True and False = False
print( not (5 > 4)) # not True = False
print((5 > 4) or (3 == 5)) # True or False = True
print(not ((5 > 4) or (3 == 5))) # Not True or False = False or False = False
print((True and True) and ( True == False)) # True and false = False
print((not False) or (not True)) # True or False = True
```

## 5. What are the six comparison operators?
```python
!=
==
>=
<=
>
<
```
## 6. What is the difference between the equal to operator and the assignment operator?

assignment operator is = and it assigns a value while == compares the values across and returns either True of False

## 7. Explain what a condition is and where you would use one.

same thing as expression but always evaluates Boolean values (True or False)
you would use them in flow control statements (eg loops)

## 8. Identify the three blocks in this code:
```python
spam = 0
if spam == 10: 
#1st block starts
print('eggs')
if spam > 5:  
    #2nd block is single line
    print('bacon')
else:
    #block 3 is single line
    print('ham') 
print('spam')
#1st block ends
print('Done') # not part of the loop
```
## 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
```python
print('enter the number')
spam = int(input('>'))

if spam == 1:
print('Hello')
elif spam == 2:
print('You have a poopy butthole')
else:
print('Greetings!') 
```

