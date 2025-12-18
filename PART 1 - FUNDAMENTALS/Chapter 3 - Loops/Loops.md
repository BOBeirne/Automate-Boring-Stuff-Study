# Loops

## While Loop

- A while loop **repeatedly executes a block of code as long as a certain condition remains True**. 
- It's **perfect for when you don't know exactly how many times you need to loop, but you know when you need to stop.**

1. Python checks the condition before each loop iteration. 
2. If it's `True`, the code block runs. 
3. Afterward, execution jumps back to the top to check the condition again.

### WARNING - Infinite Loops 

- Watch out for infinite loops, where the condition is **always True**
- You can stop a stuck program by pressing CTRL-C.

## break and continue

* `break` - This gives you a way to exit a loop immediately, even if the loop's main condition is still True. It's a way to create an "escape hatch" based on a different condition inside the loop.
* `continue` - immediately skips the rest of the code in the current iteration and jumps back to the top of the loop to check the condition again and start the next iteration.

## "Truthy" and "Falsey"

- In **certain conditions**, Python treats some values from other data types as being **equivalent to True or False.**
- `"Falsey"` - The most **common "Falsey"** values are `0`, `0.0`, and an empty string `''`
- `"Truthy"` - Every other value (like non-zero numbers and non-empty strings) is considered "Truthy." This allows you to write simpler code like `while not name:` instead of `while not name == ''`

## for Loops and the range() Function

- **for loop** is used when you want to run a block of code a **specific number of times**
- `range()` - This is the helper that makes for loops so useful. It generates a sequence of numbers that the loop iterates over.
  - `Range(5)` will **loop 5 times** (with the loop variable being 0, 1, 2, 3, 4).
  -`range(start, stop)` lets you **specify a starting and ending number**.
  - `range(start, stop, step)` lets you specify an increment (or even a negative "step" to count down).

## Importing Modules

- Python comes with a "standard library" full of modules, which are essentially collections of pre-written functions you can use.
- `import` Used to bring a module's functions into your program. For example, `import random` gives you access to functions like `random.randint()`
- `sys.exit()` - example of an imported function. You must `import sys` first, and then you can call sys.exit() to terminate your program immediately.