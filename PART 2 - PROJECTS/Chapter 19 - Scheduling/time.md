# Time module

- Use `import time` to **import** Python's built-in time module
  - `time.time()` - **returns current time in seconds** since time of calling it in float value (also called **epoch timestamp**)
  - `time.sleep()` - **suspends** execution for given number of seconds

## time.time()

- **Also called "Unix epoch timestamp"** is the number of seconds since **1970-01-01 00:00:00 UTC**
- It is **returned as a float** value

```python
import time
time.time()
# 1766249379.6268225
```

## time.ctime()

- `time.ctime()` - **returns current time in a human-readable format**

```python
import time
time.ctime()
# 'Sat Dec 20 16:49:52 2025'

this_moment = time.time()
time.ctime(this_moment)
# 'Sat Dec 20 16:52:15 2025'
```

## Profiling code

- **Epoch timestamp** (`time.time()`) it is **useful for profiling code** - measure how long it takes to run it
- to do that call `start_time = time.time()` at the beginning of code and again at the end `end_time = time.time()`and subtract difference.

```python
import time
def calc_product():
	# calculate product of first 100k nrs
	product = 1
	for i in range (1, 100001):
		product = product * i
	return product

start_time = time.time()
result = calc_product()
end_time = time.time()
print(f'It took {end_time - start_time} s to run this program')
# It took 4.307938814163208 s to run this program
```

### cProfile.run()

- Another way to profile code, provides **much higher level of detail** than simple time.time()
- To use the cProfile profiler, **pass a string of the code you want to measure to** `cProfile.run()`
- **Further info** about cProfile can be found in [Chapter 13 of "Beyond the Basic Stuff with Python"](https://inventwithpython.com/beyond/chapter13.html)

## time.sleep()

- `time.sleep()` - **suspends** execution for given number of seconds

```python
import time
for i in range(3): # repeat 3 times
	print('tick...')
	time.sleep(5) # pause for 5s
	print('tock...')
	time.sleep(2) # pause for 2s
```

