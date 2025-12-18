# Python

- Python is a High-Level programming language, it is designed to be easy to read and write for humans
- Python programs use `.py` extension
- It is a general-purpose programming language, often used for automation but can be used for almost anything from WebDev to games and scientific computing
- It is designed for beginners in programming journey
- It uses `Interpreter` instead of having to compile every time
  - because of it, it can also be changed "on the fly", while the program is running

## Interactive shell

## Math operators

* `+` (addition)
* `-` (subtraction)
* `*` (multiplication)
* `/` (division)
* `//` (integer/floor division)
* `%` (modulo/remainder)
* `**` (exponent/power of)
* `<` (less than)
* `>` (greater than)
* `<=` (less than or equal to)
* `>=` (greater than or equal to)
* `==` (equal to)
* `!=` (not equal to)

## Data types

- There are 4 main data types:
  - `Integer`
  - `Float`
  - `Boolean`
  - `String`

### Importance of data types

- Data type of a value, **dictates on how it behaves**, especially in mathematical operations like `+` or `*`
- When `+` is used with `integer` or `float` it will result in mathematical addition: `2 + 2 = 4`
- When `+` is used with two `string` values, it will `concatenate` them: `"Hello" + "World" = "HelloWorld"`
- If you try to use incorrect data type required for a specific operation, it will result in a `TypeError` error.
  - For example, it is impossible to add str to int
  - To do so you first need to convert eligible data to int or float
  - Example: `int('42')` or `float('3.14')`
- 
### Integer

- **Whole numbers**
- They do not have fractional or decimal parts.
- Example:
  - -10 
  - 42 
  - 5555

### Float

- Floating-point Numbers
- **Numbers with decimal point**
- Used to represent numbers with fractional or decimal parts.
- Example:
  - 3.14
  - -0.5
  - 10.0
  - 1.14534

### Boolean


- They have only 2 possible values: `True` or `False`
- True = 1
- False = 0

#### Boolean Operators

- You can make mathematical operations on Boolean data type:
- They are essential for construction of `if`, `elif` or `else` loops.
* `and` - returns `True` if both sides are `True`
* `or` - returns `True` if at least one side is `True`
* `not` - returns `True` if the side is `False` (reversed)
* `nor` - returns `True` if both sides are `False` (reverse `or`)

### String

- Further explained in chapter 4- See [[strings]]
- Text data, which is a sequence of characters enclosed in either single `'` or double `"` quotes.
- Example:
  - 'Hello World'
  - "Hello"
  - "12345"

## Variables



## Core Built-in functions

* `print()` - display text on the screen.
  * `print('Hello World')`
* `input()` - get text from the user.
  * `name = input('What is your name?')`
* `len()` - get the length of a string.
  * `len(name)`
* `str()`, `int()`, and `float()` to convert values between
data types.
 - `str(3)`, `int('3')`, `float('3.0')`
