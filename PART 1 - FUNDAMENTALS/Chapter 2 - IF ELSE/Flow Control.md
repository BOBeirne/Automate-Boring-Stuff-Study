# Flow control

## Boolean Values

- The two fundamental values: `True` and `False`, represent 1 and 0
- Fundamental blocks of any decision-making in logical operations
- `True` and `False` are **case sensitive**
- They are values, and they **start with an uppercase letter**
- They differentiate from strings by not using quotation marks
	- `'True'` is a string
	- `True` is Boolean value

## Comparison Operators

These comparisons always evaluate to either `True` or `False`
- `==` - equal to 
- `!=` - NOT equal to 
- `<` - less than (value on the right) 
- `>` - greater than (value on the right) 
- `<=` - less than or equal to
- `>=` - greater than or equal to

## Boolean Operators:

- You can make mathematical operations on Boolean data type:
- They are essential for construction of if, elif or else loops.
- `and` - returns True if both sides are True
- `or` - returns True if at least one side is True
- `not` - returns True if the side is False (reversed)
- `nor` - returns True if both sides are False (reverse or)

## Flow Control Statements

- The core of decision-making and repetition

### IF loop

- `if` - Executing a block of code only if the condition is `True`
- `else` - Executing a block of code if the `if` condition (or preceding `elif` conditions) is `False`.
- `elif` - (Else If) Checking additional conditions when previous ones were `False`.

### While loop

- `while` Repeating a block of code as long as a condition remains `True`.

### Break and Continue

- `break` - Use it to immediately exit a loop.
- `continue` Skip the rest of the current loop iteration and going to the next one.