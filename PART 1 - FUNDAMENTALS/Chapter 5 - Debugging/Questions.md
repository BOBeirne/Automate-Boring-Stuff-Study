## Q1 Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
```python
print('enter a nr')
spam = int(input('>'))

assert spam >= 10 # assert that nr i more than 10 and if its less then it crashes
print(spam)
```

## Q2 Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)
```python
print('enter 2 different words')
eggs = input('>').lower()
spam = input('>').lower()

assert eggs != spam # words are the same!!
```
## Q3 Write an assert statement that always triggers an AssertionError.
```python
assert False # assertion error
```
## Q4 What two lines must your program have to be able to call logging.debug()?
```python
import logging 
logging.basicConfig(level=logging.DEBUG)
```
## Q5 What two lines must your program have to make logging.debug() send a logging message to a file named programLog.txt?
```python
import logging 
logging.basicConfig(filename='programlog.txt')
```
## Q6 What are the five logging levels?

logging levels: 
* debug,
* info, 
* warning, 
* error, 
* critical

## Q7 What line of code can you add to disable all logging messages in your program?
```logging.disable(logging.CRITICAL)``` will suppress all log messages at that level or lower

## Q8 Why is using logging messages better than using print() to display the same message?

because you can filter different levels of error messages

## Q9 What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

* **step over** = Executes the code on the current line. If it's a function call, it runs the entire function and stops at the next line in the current scope.
* **step in** = If the current line is a function call, it moves the debugger to the first line inside that function.
* **step out** = Finishes executing the current function and stops at the line where the function was originally called.


## Q10 After you click Continue, when will the debugger stop?

At the end of program or another break point

## Q11 What is a breakpoint?

Tells debugger where to stop the program to allow you investigate further

## Q12 How do you set a breakpoint on a line of code in Mu?

You click on the line until red dot appears
