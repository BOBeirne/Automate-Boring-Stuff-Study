## Boolean Values

1) For each of the following, answer "yes" if it is a Python Boolean value and "no" if it is not.

- False - yes
- 'True' - no, str
- false - no, lowercase
- True - correct
- 'false' - no, str
- true - no, lowercase

---

##  Comparison Operators

1) Answer "yes" if it is a Python comparison operator and "no" if it is not.

- = - no, assignment operator
- < - yes
- => - wrong order, should be <=
- =! - wrong order, should be !=
- != - correct
- == - correct
- `>` - correct 
- <= - correct

2) What is the difference between the < and <= operators?

the <= also accepts the "equal" value, while `<` does not, everything has to be under the specified value

3) What is the difference between the = and == operators?

the = is equal, used to assign value to a variable
== is a comparison and returns a boolean value True if both sides evaluate equally, False if they are different

4) Why does 42 == 42.0 evaluate to True?

they have same value

5) Why does 42 == '42' evaluate to False?

one is int, the other is a str

6) What happens if you enter 42 < 'hello' into the interactive shell?

You get type error, can't use that operation between str and int

---

## Boolean Operators

1) Draw the truth tables for the Boolean operators below.

- and

TRUE AND TRUE = TRUE
TRUE AND FALSE = FALSE
FALSE AND TRUE = FALSE
FALSE AND FALSE = FALSE

- or

TRUE OR TRUE = TRUE
TRUE OR FALSE = TRUE
FALSE OR TRUE = TRUE
FALSE OR FALSE = FALSE

- not

NOT TRUE = FALSE
NOT FALSE = TRUE


2) What do the following expressions evaluate to?

- 2 + 2 > 4 or True = TRUE
- True and 2 + 2 >= 4 = TRUE
- True and (True or False) = TRUE
- (False or True) and True = TRUE
- True and not False = TRUE
- not (False or True) FALSE
- not False or True = TRUE
- True and True and True and True and False = FALSE
- False or False or False or True or False = TRUE

3) Say the variable `is_raining` is set to either True or False. Describe what is_raining = not is_raining does.

it's changing (toggling) the boolean value of the variable is_raining from true to false

4) If the variable name has the value 'Alice', which expression is correct: name == 'Alice' or name == 'Bob' or name == 'Alice' or 'Bob'?

name == 'Alice' = TRUE
name == 'Bob' = FALSE
name == 'Alice' or 'Bob' = TRUE

---

## Components of Flow Control

1) When does a new block begin?

any line that ends with `:`

2) Can a block be inside another block?

yes

3) A new block is expected after statements that end with what character?

:

4) When does a block end?

when indentation level decreases a level

5) What is the program execution?

active step of program being processed - current line python is on as it runs through the code

---
## Questions below relate to the following program:

```python
name = 'Alitza'
if name == 'Dolly':
    print('Hello, Dolly!')
print('Done')
```

1) How many blocks are in this program?

1

2) On what line does the first block begin?

`if name == 'Dolly':`

On what line does the first block end?
`print('Done')`

---

## Flow Control Statements

1) Answer "yes" if the following are valid if statements, given eggs = 12. Answer "no" if not.

- if eggs = 12: # no, single = is assignment
- if eggs > 12 # no, missing :
- if: # no
- if eggs == 12: # yes
- if eggs != 'hello': # yes
- if eggs < 12: # yes

2) Answer "yes" if the following are valid else statements, given they follow if eggs == 12: and its block. Answer "no" if not.

- else: # yes
- else if eggs != 12: # no
- else # no, missing :
- else if not: # not valid python syntax
- else not: # same

3) Answer "yes" if the following are valid elif statements, given they follow if eggs == 12: and its block. Answer "no" if not.

- elif: # no, you need to specify condition in elif
- elif eggs != 12: # yes
- else if eggs != 12: # not a valid python syntax
- elif eggs == 12: # yes

4) Examine the following flawed program:

```python
password = 'swordfish'
if password == 'rosebud':
    print('Access granted.')
else:
    print('Access denied.')
elif password == 'swordfish':
    print('That is the old password.')
```

    1) Why does this program cause an error?

elif should be second block, execution stops after else so elif is never checked

    2) How many elif statements can follow an if statement and its block?

no limit if you don't care about you'r program's performance