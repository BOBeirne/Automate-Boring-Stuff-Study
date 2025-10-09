'''
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password has several rules:

* it must be at least eight characters long,
* contain both uppercase and lowercase characters,
* and have at least one digit.

Hint: It’s easier to test the string against multiple regex patterns than to try to come up with a single regex that can validate all the rules.
'''

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


print(f"password, {pw}, is valid:")
print(f"Has eight+ chars: {eight_char(pw)}")
print(f"Has upper letters: {uppercase(pw)}")
print(f"Has lower letters: {lowercase(pw)}")
print(f"Has digits: {digit_check(pw)}")