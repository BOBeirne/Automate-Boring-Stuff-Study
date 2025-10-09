
# Practice Test

## Questions

### 1.  What is the function that returns Regex objects?

re.compile()

### 2.  Why are raw strings often used when creating Regex objects?

to remove any formatting characters as some of them are used for regex and need to be escaped
this wouldn't work in a normal string

### 3.  What does the search() method return?

it returns "Match" object in the provided string if it finds a match
"None" if there is no match

### 4.  How do you get the actual strings that match the pattern from a Match object?

.group()

### 5.  In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

* group 0 is the whole length of the regex (\d\d\d)-(\d\d\d-\d\d\d\d)
* group 1 (\d\d\d)
* group 2 (\d\d\d-\d\d\d\d)

### 6.  Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

* if i want to match actual dot i need to escape it using backslash \.
* to escape parentheses you would use \( and \)
* . matches any character except for a newline

### 7.  The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

* if regex has no groups it will return list of strings
* it will return tuples if regex has groups

### 8.  What does the | character signify in regular expressions?

* pipe means "either or"
* it can be used to search for multiple options of regex at once

### 9.  What two things does the ? character signify in regular expressions?

* "?" is used in regex to specify an optional character or making a match lazy

### 10.  What is the difference between the + and * characters in regular expressions?

* symbol + matches one or more same type of specified condition, so \d+ would mean "one or more digits", equivalent of {1,}
* * it means "0 or more" equivalent of {0,}

### 11.  What is the difference between {3} and {3,5} in regular expressions?

* {3} means "match exactly 3"
* {3,5} means "match from 3 to 5 of instances"

### 12.  What do the \d, \w, and \s shorthand character classes signify in regular expressions?

* \d is digit
* \s is single whitespace character
* \w is word character and underscore

### 13.  What do the \D, \W, and \S shorthand character classes signify in regular expressions?

* they are the opposites of \d, \s and \w
* so \d matches all digits, \D will match everything but digits

### 14.  What is the difference between the `.*` and `.*?` regular expressions?

it changes result from greedy mode to lazy mode

### 15.  What is the character class syntax to match all numbers and lowercase letters?

[a-z0-9]

### 16.  How do you make a regular expression case-insensitive?

re.IGNORECASE or re.I

### 17.  What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

it's a way to search all characters including newline as . does not include newline chars

### 18.  what will this code return?

``` python
num_re = re.compile(r'\d+')
num_re.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')
```

it will replace any digits with "X"

### 19.  What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

* it allows to split the regex over multiple lines for easier readability
* it also allows you use python syntax inside a regex so you can add comments

## Practice Programs

For practice, write programs to do the following tasks.

### Strong Password Detection

Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password has several rules:

* it must be at least eight characters long,
* contain both uppercase and lowercase characters,
* and have at least one digit.

Hint: It’s easier to test the string against multiple regex patterns than to try to come up with a single regex that can validate all the rules.

``` python
import re
pw = input('Provide a password: ')

def eight_char(password):
    len_regex = re.compile(r'^.{8,}$')
    len_check = len_regex.search(password)
    return bool(len_check)

def uppercase(password):
    upper_regex = re.compile(r'[A-Z]')
    upper_check = upper_regex.search(password)
    return bool(upper_check)

def lowercase(password):
    lower_regex = re.compile(r'[a-z]')
    lower_check = lower_regex.search(password)
    return bool(lower_check)

def digit_check(password):
    digit_regex = re.compile(r'[0-9]')
    digit_match = digit_regex.search(password)
    return bool(digit_match)


print(f"{pw}, is valid:")
print(f"Has eight+ chars: {eight_char(pw)}")
print(f"Has upper letters: {uppercase(pw)}")
print(f"Has lower letters: {lowercase(pw)}")
print(f"Has digits: {digit_check(pw)}")
```

### Regex Version of the strip() Method

Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then the function should remove whitespace characters from the beginning and end of the string. Otherwise, the function should remove the characters specified in the second argument to the function.

``` python

import re

str_to_process = input('Enter a string: ')
chars_to_remove = input('Any chars to remove?: ')

def strip_method(str_to_process, chars_to_remove = None):
    if not chars_to_remove:
        REGEX_STR = re.compile(r'^\s+|\s+$')
        strip_str = REGEX_STR.sub('', str_to_process)
        return strip_str
    else:
        # gotta fix stuff here
        REGEX_STR = re.compile(f'(^[{chars_to_remove}]+)|[{chars_to_remove}]+$')
        strip_str = REGEX_STR.sub('', str_to_process)
        return strip_str
    
    
print(f"Processed string: ", strip_method(str_to_process, chars_to_remove))
```
