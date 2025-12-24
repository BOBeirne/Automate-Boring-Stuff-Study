# Practice Questions

  1.  What is the Unix epoch?

it's a moment in time -  1st of Jan of 1970 00:00:00

  2.  What function returns the number of seconds since the Unix epoch?

`time.time()`

  3.  What time module function returns a human-readable string of the current time, like 'Mon Jun 15 14:00:38 2026'?

`time.ctime()`

  4.  How can you pause your program for exactly five seconds?

`time.sleep(5)`

  5.  What does the round() function return?

`round()` rounds up a float value to integer value
you can pass it an integer value of how many decimal point you'd like it to round the value to
it rounds to nearest even number instead of simply rounding up or down.
- so `2.5` will round to `2`
- `4.5` will round to `4`
- `5.5` will also round to nearest even value neighbor - `6` instead of `5`


  6.  What is the difference between a datetime object and a timedelta object?

`datetime` object represents a specific moment in time
`timedelta` object represents a period of time. It can be used to calculate a **difference** between 2 `datetime` objects

  7.  Using the datetime module, what day of the week was January 7, 2019?

```python
import datetime as dt
jan7 = dt.datetime(2019, 1, 7, 0, 0, 0)
print(jan7.strftime('%A'))
```

Monday.