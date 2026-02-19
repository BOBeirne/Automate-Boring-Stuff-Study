## Entering Expressions into the Interactive Shell

- Entering code into the interactive shell lets you experiment with running instructions one at a time. At the >>> prompt, you can enter expressions made up of values, operators, and other Python code. After running the code, the interactive shell prints the result.

1)  Match the names for questions 1 through 7 to these math operators:

`+  -  *  /  **  //  %`

Division `/`

Multiplication `*`

Subtraction `-`

Modulo `%`

Addition `+`

Exponentiation `**`

Floor division `//`

---

2) Is there a difference in how Python interprets these two expressions?

`2 + 2 and 2        + 2`

no, ignores whitespaces in expressions

3) If the expression 26 / 8 evaluates to 3.25, what does the expression 26 // 8 evaluate to?

`3` as it removes the remainder

4) 26 divided by 8 is 3 with a remainder of 2. What does the expression 26 % 8 evaluate to?

`2`

5) Write the expression that adds the numbers 1 to 10. (Hint: It begins with 1 + 2 + 3 + and so on.)

x = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10

6) Which of the two operators in the following expressions is evaluated first according to Python’s order of operation rules?

```text
(4 + 5) * 6   - the ones inside brackets

2 ** 3 + 1 - the one with **

1 + 2 ** 3 - the one with **

(1 + 2) ** 3 - inside brackets

2 + 4 + 6 - 2 + 4 (from left to right)
```

7) Which of the following expressions produce errors? (You can enter them into the interactive shell to check.)

- `2 + `  - missing 2nd argument

- `42` - fine

- `((3 + 1) * 2)` - fine

- `((3 + 1 * 2)` - missing closing bracket

- `(0)` - fine

- 1 + 2 3 - it must be either 23 or calculation between 2 and 3

## The Integer, Floating-Point, and String Data Types

1) Label the data types of the values in questions 23 through 29 as either int, float, or string. Hint: You can pass them to the type() function in the interactive shell to find the answers, such as type(2) or type('hello').

- `2` - int

- `-2` - int

- `2.0` - float

- `'hello'` - str

- `2.2` - float

- `'2'` - str

- `'2.2'` - str

2) What is the difference between the values 10, 10.0, and '10'?

- `10` is int
- `10.0` is float
- `'10'` - is a str

## String Concatenation and Replication

1)  What do the following expressions evaluate to?

- `'Hello' + 'Hello' + 'Hello'` - `'HelloHelloHello'`

- `'Hello' * 3` - `'HelloHelloHello'`

- `3 * 'Hello'` - `'HelloHelloHello'`

- `(2 * 2) * 'Hello'` - `'HelloHelloHelloHello'`

- `'13' + '12'` - `'1312'`

# Which of the following expressions produce errors?

- `'Forgot the closing quote` - this one

- `'Hello' * 3.0` - dont think you can calculate str with float? 

- `'Hello' + 3` - can't append str to int, need to first make int a str - str(3)

- `Hello + Hello + Hello` - they need their quotes, otherwise hello will error out as NameError

- `'Alice' * 'Bob'` - can't multiply strings by strings

- `'Hello' / 5` - can't divide str

- 'Hello' / 'Hello' - unsure, i feel like division on str is still a nono

# Storing Values in Variables

The following programs store values in variables. Determine what each program outputs.


```python
nephew = 'Jack'
print(nephew)
# Jack


nephew = 'Jack'
print('nephew')
# nephew

nephew = 'Jack'
nephew = 'Albert'
print(nephew)
# Albert

nephew = 'Jack'
Nephew = 'Albert'
print(nephew)
# Jack
```

2) Why do the following programs cause an error?

```python
nephew = Jack # python treats Jack as another variable, not str
print(nephew) 


nephew = 'Jack'
print(Jack) # there is no variable named Jack


nephew = 'Jack'
print(NEPHEW) # no variable named NEPHEW - capitalization matters

print(nephew)  # no variable defined named nephew
```

3) Which of the following are valid variable names?

```python

number_of_cats # yes

number-of-cats # substraction operator cannot be used in var names

numberofcats #yes

numberOfCats # yes

_42 # yes

_ # valid, also called "throwaway" variable

42 # int by itself cannot be variable, you can assign variable to it though
```


## Your First Program

1) Label the following as a variable, function call, or string.

```python
'hello' # str

hello # var

print() # function call

'print()' # str
```

2) Do the following expressions cause an error or no error? If they cause no error, what do they evaluate to?

```python
int('42') # you can turn this str into 42 int

int('forty two') # this one cannot be converted

int('Hello') #  # this one cannot be converted

int(-42) # this is int

int(3.1415) # fine

float(-42) # fine

str(-42) # fine

str(3.1415) # fine

str('Hello') # this is correct

str(float(int(3.14))) # fine

str(3) #fine

str(3.0) # fine
```

3) Why does this two-line program cause an error?

```python
number_of_cats = 4
print('I have ' + number_of_cats)
# can't add str to in, need to convert var to str
```

4) Does round(4.9) evaluate to the integer 5 or the float 5.0?

int (cause you're rounding)

5) Describe what the abs() function returns.

returns absolute value (positive)

6) What does abs(5) return?

5

7) What does abs(-5) return?

5

## How Computers Store Data with Binary Numbers

1) Why do computers use the base-2 binary number system instead of the more familiar base-10 decimal system humans use?

because at the core they use electrical current where 0 is no electricity and 1 is power on

2) How many bits are in 1 byte?

8?

3) Determine how many bytes the units represent, both as an exponent like 210 and a whole number like 1,024. You can enter an expression like 2 ** 10 into the interactive shell to calculate 210.

```python
Kilobyte # 2 ** 10 = 1024

Megabyte # 2 ** 20 = 1048576

Gigabyte # 2 ** 30 = 1073741824

Terabyte # 2 ** 40 = 1099511627776
```

4) Decimal 2 is 10 in binary. What is decimal 3 in binary?

`11`?

5) Decimal 7 is 111 in binary. What is decimal 8 in binary?

`1000`?