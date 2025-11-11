"""
Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, 
then the function should remove whitespace characters from the beginning and end of the string. 
Otherwise, the function should remove the characters specified in the second argument to the function.
"""

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