# datetime module

- Use `import datetime` to **import** Python's built-in datetime module
- It's helpful to display date in easier to read format or to do **arithmetics on dates**
- It has it's own **datetime data** type
  - each value represents a specific moment in time
  - it has **year**, **month**, **day**, **hour**, **minute**, **second**, **microsecond**

```python
import datetime
datetime.datetime.now()
# datetime.datetime(2025, 12, 20, 21, 2, 1, 858861)
dt = datetime.datetime(2026, 2, 27, 16, 30, 0)
dt.year, dt.month, dt.day
# (2026, 2, 27)
dt.hour, dt.minute, dt.second
# (16, 30, 0)
```

## Unix Epoch with datetime

- You can convert epoch into datetime object using `datetime.datetime.fromtimestamp()`
- it will be returned with a current time zone

```python
import datetime as dt
import time

dt.datetime.fromtimestamp(1000000) # 1m seconds after epoch
# datetime.datetime(1970, 1, 12, 13, 46, 40)
dt.datetime.fromtimestamp(time.time()) # current timestamp converted into dt format
# datetime.datetime(2025, 12, 20, 22, 16, 16, 677509)
dt.datetime.now() # SAME AS ABOVE
# datetime.datetime(2025, 12, 20, 22, 16, 16, 677509)
```

## timedelta()

- `datetime.timedelta()` is used to **calculate the difference** between **two datetime objects**
- it can be used to **calculate the difference** between **two dates**
- It takes arguments for: weeks, days, hours, seconds, miliseconds and microseconds
- It does NOT have any year or month arguments
- it returns a timedelta object with days, seconds and microseconds
- `total_seconds()` returns seconds only
- pass it to `str()` and it will print out in more readable format
- `timedelta` handles all leap years and how many days are in each month for you so you don't need to remember it

```python
import datetime as dt
delta = dt.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
# (11, 36548, 0)
delta.total_seconds() # print out seconds only
# 986948.0
str(delta) # print out nicely formatted timedelta
# '11 days, 10:09:08'
```

### timedelta arithmetics

- `timedelta` can be used to **calculate the difference** between **two datetime objects**
- You can use `+` and `-` operators but also multiply and divide using `/` or `*` by `integer` or `float`

```python
import datetime as dt

oct21st = dt.datetime(2026, 10, 21, 16, 29, 0)
around30yrs = dt.timedelta(days=365*30)
print(oct21st)
# 2026-10-21 16:29:00
print(oct21st - around30yrs)
# 1996-10-28 16:29:00
print(oct21st - (2 * around30yrs))
# 1966-11-05 16:29:00
```

## Pausing until specific date

- You can use while loop to **pause** your program until a specific date

```python
import datetime as dt
import time as t

halloween2039 = dt.datetime(2039, 10, 31, 0, 0, 0)

while dt.datetime.now() < halloween2039:
	t.sleep(1) # pause for 1 second before looping and checking again
	print('Not halloween yet, will check again soon..')
```

## strftime()

- [Docs](https://strftime.org/)
- `strftime()` is a **string formatting** function
- You can pass it desired formatting and it will print out a formatted string


| `strftime()` directive | Meaning                                        |
|----------------------|------------------------------------------------|
| `%Y `                  | Year with century, as in '2026'                |
| `%y`                   | Year without century, '00' to '99' (1970 to 2069) |
| `%m`                   | Month as a decimal number, '01' to '12'        |
| `%B`                   | Full month name, as in 'November'              |
| `%b`                   | Abbreviated month name, as in 'Nov'            |
| `%d`                   | Day of the month, '01' to '31'                 |
| `%j`                   | Day of the year, '001' to '366'                |
| `%w`                   | Day of the week, '0' (Sunday) to '6' (Saturday) |
| `%A`                   | Full weekday name, as in 'Monday'              |
| `%a`                   | Abbreviated weekday name, as in 'Mon'          |
| `%H`                   | Hour (24-hour clock), '00' to '23'             |
| `%I`                   | Hour (12-hour clock), '01' to '12'             |
| `%M`                   | Minute, '00' to '59'                           |
| `%S`                   | Second, '00' to '59'                           |
| `%p`                   | 'AM' or 'PM'                                   |
| `%%`                   | Literal '%' character                          |


```python
import datetime as dt
oct21st = dt.datetime(2026, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
# '2026/10/21 16:29:00'
oct21st.strftime('%B of %y')
# 'October of 26'
```

## strptime()

- [Docs](https://strftime.org/)
- You can use this function to **convert a string to a datetime object**
- It's the exact **reverse of `strftime()` function**
- You can convert strings such as `'2026/10/21 16:29:00'` or `'October 21, 2026'` to a `datetime` object
- You need to pass it exact formatting to help it understand how to translate the string

Example of how to use the `strptime()` function
```python
import datetime as dt

dt.datetime.strptime('October 21, 2026', '%B %d, %Y')
# datetime.datetime(2026, 10, 21, 0, 0)
dt.datetime.strptime('2026/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
# datetime.datetime(2026, 10, 21, 16, 29)
dt.datetime.strptime("October of '26", "%B of '%y")
# datetime.datetime(2026, 10, 1, 0, 0)
dt.datetime.strptime("November of '63", "%B of '%y")
# datetime.datetime(2063, 11, 1, 0, 0)
dt.datetime.strptime("November of '73", "%B of '%y")
# datetime.datetime(1973, 11, 1, 0, 0)
```