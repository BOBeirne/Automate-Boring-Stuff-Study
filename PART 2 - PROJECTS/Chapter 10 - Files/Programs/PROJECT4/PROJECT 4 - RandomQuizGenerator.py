"""Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

Here is what the program does:

Creates 35 different quizzes
Creates 50 multiple-choice questions for each quiz, in random order
Provides the correct answer and three random wrong answers for each question, in random order
Writes the quizzes to 35 text files
Writes the answer keys to 35 text files
This means the code will need to do the following:

Store the states and their capitals in a dictionary.
Call open(), write(), and close() for the quiz and answer key text files.
Use random.shuffle() to randomize the order of the questions and multiple-choice options.
Let’s get started.

Step 1: Store the Quiz Data in a Dictionary
The first step is to create a skeleton script and fill it with your quiz data. 
Create a file named randomQuizGenerator.py, and make it look like the following:"""


# Creates quizzes with questions and answers in random order, along with the answer key

import random
from pathlib import Path
import os

os.chdir('F:\\Python\\Automate boring stuff\\PART 2 - PROJECTS\\mod 10\\PROJECT4')

# Quiz data, Keys - states and values - capitals
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau', 
    'Arizona':'Phoenix', 
    'Arkansas': 'Little Rock', 
    'California': 'Sacramento', 
    'Colorado':'Denver', 
    'Connecticut': 'Hartford', 
    'Delaware': 'Dover', 
    'Florida': 'Tallahassee', 
    'Georgia': 'Atlanta', 
    'Hawaii': 'Honolulu', 
    'Idaho': 'Boise',
    'Illinois': 'Springfield', 
    'Indiana': 'Indianapolis', 
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 
    'Kentucky': 'Frankfort', 
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 
    'Maryland': 'Annapolis', 
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 
    'Minnesota': 'Saint Paul', 
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 
    'Montana': 'Helena', 
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 
    'New Hampshire': 'Concord', 
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 
    'New York': 'Albany', 
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 
    'Ohio': 'Columbus', 
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 
    'Pennsylvania': 'Harrisburg', 
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 
    'South Dakota': 'Pierre', 
    'Tennessee': 'Nashville', 
    'Texas': 'Austin', 
    'Utah': 'Salt Lake City', 
    'Vermont': 'Montpelier', 
    'Virginia': 'Richmond', 
    'Washington': 'Olympia', 
    'WestVirginia':'Charleston', 
    'Wisconsin': 'Madison', 
    'Wyoming': 'Cheyenne' }
    
# create 35 quiz files

for quiz_nr in range(35):
    
    # create quiz and answer key files
    quiz_file = open(f'capitalsquiz{quiz_nr + 1}.txt', 'w', encoding='utf-8' )
    answer_file = open(f'capitalsquiz_answ{quiz_nr + 1}.txt', 'w' , encoding='UTF-8')
    
    # write out header for the quiz
    quiz_file.write('Name:\n\nDate:\n\nPeriod\n\n')
    quiz_file.write((' '*20) + f'State Capitals Quiz (Form: {quiz_nr +1})')
    quiz_file.write('\n\n')
    
    # shuffle the order of states (keys)
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all 50 states making question for each
    for nr in range(50):

         # get right or wrong answers
         correct_answ = capitals[states[nr]] # get the correct answer
         wrong_answ = list(capitals.values()) #  pull out all possible answers
         del wrong_answ[wrong_answ.index(correct_answ)] # delete the correct answ from the pool
         wrong_answ = random.sample(wrong_answ, 3) # pick random 3 wrong answers
         answer_options = wrong_answ + [correct_answ] # add wrong answ to the pool pf potential answers
         random.shuffle(answer_options) # randomize the way choices are displayed

         # write q and answ options to the quiz file
         quiz_file.write(f'{nr+1}. Capital of {states[nr]}:\n')
         for i in range(4):
             quiz_file.write(f"     {'ABCD'[i]}. {answer_options[i]}\n")
         quiz_file.write('\n')

         # write answ key to the file
         answer_file.write(f"{nr+1}.{'ABCD'[answer_options.index(correct_answ)]}")

    quiz_file.close()
    answer_file.close()
