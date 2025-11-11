"""
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.
The program would find these occurrences and prompt the user to replace them:

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
It would then create the following text file:

The silly panda walked to the chandelier and then screamed. A nearby
pickup truck was unaffected by these events.
"""

import re # to search for parts of strings and use .sub() method
from pathlib import Path # to operate on the files

REGEX = re.compile(r'ADJECTIVE|NOUN|VERB') # regex targeting specific keywords

#file_content = open(Path('Madlibs.txt'),'r') # open the original file
#original_str = file_content.read() # read the file and put it in the variable
#file_content.close() # close the file after you extract the data needed
original_str = Path('Madlibs.txt').read_text() # replacing with one simple pathlib line


placeholders = REGEX.findall(original_str) # use findall() on original string to find all placeholders and store thm in a list

user_inputs = [] # empty list ready for inputs from user

def replace_words(original_str,user_inputs): # function that processes the keywords on the original string
    for replacement in user_inputs: # go through list or replacement keywords
        original_str = REGEX.sub(replacement, original_str, count=1) # replace the words one by one and update original string
    return original_str


print(f'This is the original string\n')
print(f'{original_str}')

# ask user for input and add each into the list for placeholder replacements
for word_type in placeholders:
    user_input = input(f'Enter an {word_type.lower()}: ')
    user_inputs.append(user_input)

print(f'This is a new string: \n')
new_madlibs = replace_words(original_str,user_inputs)
print(new_madlibs)

Path('MadLibs_new.txt').write_text(new_madlibs) # write the final str into new file
print('New story saved to MadLibs_new.txt')

