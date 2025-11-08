# Loops
## 1. What keys can you press if your Python program is stuck in an infinite loop?

ctrl+c

## 2. What is the difference between break and continue?

```break``` stops the execution of the loop

```continue``` skips whatever code is after in the current loop and skips to the next iteration of the loop

## 3. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

no difference

## 4. Write a short program that prints the numbers 1 to 10 using a for loop. Then, write an equivalent program that prints the numbers 1 to 10 using a while loop.

### for loop
```python
for i in range(1, 11):
    print(i)
``` 

### while loop 
```python
i = 1   
while (i < 11):
    print(i)
    i += 1
```

## 5. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

```spam.bacon()``
