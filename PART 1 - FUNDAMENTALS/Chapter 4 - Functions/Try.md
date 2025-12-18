# Try and Except

- Try and except are used to **handle errors in a program instead of it simply crashing**
- It is made of 2 blocks, `try` and `except`
  - `try` is where you put code which could potentially crash
  - `except` is an instruction on how to handle the crash error gracefully

## Try 

- This is where you **put the potentially crashing code**
- Python will try an execute the code

## Except

- This is where the programs handles **any kind of error**
- There are **many types of `except` errors**, you can use simple except to catch them all or specify a particular type to catch.


- The most common ones are: 
  - `ValueError` - when a function receives an arg of **inappropriate value** (trying to **convert str to int**)
  - `TypeError` - If you try to for example add a **string to a number**
  - `ZeroDivisionError` - if you try to **divide by 0**
  - `IndexError` - if you try to access an **index that does not exist**
  - `KeyError` - if you try to access a **key that does not exist**
  - `NameError` - if you try to access a **variable that does not exist**
  - `AttributeError` - if you try to access an **attribute that does not exist**
  - `IOError` - if you try to **read or write to a file that does not exist**
  - `FileNotFoundError` - if you try to **open a file that does not exist**

- To **catch the error message** use `except Exception as err:`