# Functions
## 1. Why are functions advantageous to have in your programs?

* you can make a piece of job that you want to apply to changing variables and then the program to do that job only on those variables when called
* by defining multiple functions for different jobs its also easier to organize the code and figure out where are the issues
* you can also make functions trigger each other making a cascading order of events to operate on specified value

## 2. When does the code in a function execute: when the function is defined or when the function is called?

called

## 3. What statement creates a function?

```def function():```

## 4. What is the difference between a function and a function call?

function def defines the actual job the function needs to do while calling the function is asking that part of program to run on the variables specified

## 5. How many global scopes are there in a Python program? How many local scopes are there?

each function has their own local scope but they can also call on global scope or you can define a global scope inside the function but there is only one global scope

## 6. What happens to variables in a local scope when the function call returns?

they get cleared from memory and forgotten

## 7. What is a return value? Can a return value be part of an expression?

at the end of function you return the value it can be an int, str etc
it can be a part of expression eg. total = 10 + my_function()

## 8. If a function does not have a return statement, what is the return value of a call to that function?

it returns None

## 9. How can you force a variable in a function to refer to the global variable?

yes by specifying global

## 10.  What is the data type of None?

NoneType

## 11. What does the import areallyourpetsnamederic statement do?

imports a module under that name if it is installed

## 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

```spam.bacon()```

## 13. How can you prevent a program from crashing when it gets an error?

use try and except to raise an exception if there is an issue to avoid program crashing

## 14. What goes in the try clause? What goes in the except clause?

in try clause goes the code to try, in except clause goes the code to run if the code fails

## 15. Write the following program in a file named notrandomdice.py and run it. Why does each function call return the same number?
```python
import random 
def get_random_dice_roll():
    random_nr = random.randint(1,6) # this needs to be inside function
    return random_nr

print(random_nr) 
```