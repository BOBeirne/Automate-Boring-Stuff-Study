# Function

- Functions a like **mini-programs within your main program**. They are a **block of code to do a specific task**.
- They are **great for breaking up your code into smaller parts** and reusing code without having to copy/paste it.
- You can **call a function multiple times**, you call it by calling it's name and parenthesis `functionName()`
- They can take arguments inside parenthesis and can **return values using `return` keyword**

Example of simple function:
```python
def sayHello():
	print('Hello!')

sayHello()
# Hello!
```

## Parameter

- Parameters are the **arguments that a function accepts.**
- They are **placeholders for values** that will be passed to the function when it is called.
- You can **name the parameters anything you want**, but it's common to name them something descriptive.


## Argument

- Arguments are the **values that are passed to the function when it is called**.
- They **replace the Parameter** in the function definition.

Example of calling function with and Argument:

```python
greet_user('Alice') # Alice is an argument
greet_user('Bob') # Bob is an argument
```

- When you call `greet_user('Alice')` the name parameter inside gets assigned the value 'Alice'

## Return

- A return statement is a way to **exit a function and return a value** to the caller.
- It **sends a value back to the caller** of the function.
- if there is **no return statement**, it will return `None`

```python
# This function displays a result of a + b
def display_sum(a, b):
	print( a + b ) # There is no return, so the value returned is None

def calculate_sum(a, b):
	return a + b

# This function has no return so None gets returned
sumab = display_sum(2, 3) # this function call only prints 5
print(sumab) # but the actual value it returns is...
# None

# This function is returning a value
result = calculate_sum(2, 3)
print(result)
# 5
# We can even make operations on it!
new_total = result + 10 #  we can make operations here
print(new_total)
# 15
print(result * 2) # and here!
# 10
```

## Scope

### Local Scope

- Variables created **inside the function (incl it's parameters) are called local variables**.
- They **exist only inside that function**
- When **function** finishes and **returns**, those **variables are forgotten**

### Global scope

- Variables created **outside all functions** are called global variables.
- They can be **read and accessed anywhere in the script**, including inside any function

```python

spam = 'I am a global variable' # This is a global variable

def some_function():
	spam = 'I am local variable' # This is local variable, only accessible inside this function
	print(spam) # this will print local variable

some_function()
print(spam) # This will print global variable
```

### Global variable

- A global variable is a **variable that is defined outside of any function but can be modified inside the function.**

Example:
```python
spam = 'I am a global variable' # This is a global variable

def some_function():
	spam = 'I am local variable' # This is local variable, only accessible inside this function
	spam = 99
	print('Inside some_function without global variable:', spam) # this will print local variable

def some_function_with_global():
	global spam # this is a global variable, we modify the global spam
	spam = 101
	print('Inside some_function_with_global with global variable:', spam) # this will print global variable

print('Before calling any functions, global spam is:', spam) # this will print global variable before modification

some_function()
print('After using some_function(), global spam is still:', spam) # this will print global variable after function runs

some_function_with_global()
print('After using some_function_with_global(), global spam is now:', spam) # this will print global variable after function runs
```

## Nested functions

- You can have a **function defined inside another function**

```python
def outer_function():
	print('I am an outer function')

	def inner_function():
		print('I am an inner function')

	inner_function() # You can only call the inner function from within the outer function

outer_function()
# inner_function # <- This would cause an error because you can't call the inner function outside of the outer function
```

## Function call stack

- think of it like a **stack of plates** or sticky notes, it's how program remembers where is it in the program.

1. When program starts the stack is empty
2. When a function is called, it is pushed onto the stack
3. If a function calls another function, it is pushed onto the top of the previous function
4. When a function returns, it is popped off the top of the stack
5. Program now looks at the top of the stack and executes the next line of code

```python
def a():
	print('a() starts')
	b()
	d()
	print('a() returns')

def b():
	print('b() starts')
	c()
	print('b() returns')

def c():
	print('c() starts')
	print('c() returns')

def d():
	print('d() starts')
	print('d() returns')

a()
```
###  The Call Stack and Error Messages

- **Traceback in error messages** is the call **stack location**, it will tell you in which function did the error happened

```text
Traceback (most recent call last):
File "C:/Users/Al/example.py", line 13, in <module>
	a()
```
Signals that the error happened in the function a