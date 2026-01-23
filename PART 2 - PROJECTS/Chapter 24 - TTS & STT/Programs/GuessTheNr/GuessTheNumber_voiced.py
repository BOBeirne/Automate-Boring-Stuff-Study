""" 
Adding Voice to Guess the Number
Revisit the guess the number game from Chapter 3 and add a voice feature to it. 
Replace all of the function calls to print() with calls to a function named speak(). 
Next, define the speak() function to accept a string argument (just like print() did), but have it both print the string to the screen and say it out loud. 
For example, you’ll replace this line of code

print('I am thinking of a number between 1 and 20.')

with this line of code:

speak('I am thinking of a number between 1 and 20.')

To make full use of the speech-generation feature, let’s change the 'Your guess is too low.' and 'Your guess is too high.' text to say the player’s guess. 
For example, the computer should say, 

“Your guess, 42, is too low.” 
"""


# guess the nr game
import random, pyttsx3


def speak(text):
	engine = pyttsx3.init() # initialise the engine
	engine.say(text) # queue the speech text
	engine.startLoop(False) # Start event loop in non-blocking mode
                            # False = don't block, let us control iteration
                            # True = would block like runAndWait() - runAndWait() does steps 3-7 internally, but doesn't clean up properly between calls
	engine.iterate() # start the speech
	while engine.isBusy(): # while audio is playing...
		engine.iterate()	# process the events until it finishes
	engine.endLoop() # clean up the event loop



secret_nr = random.randint(1, 100)
speak('Im thinking of nr between 1 and 100')

# ask to guess 6 times
for guesses_taken in range(1, 10):
	speak('Take a guess')
	guess = int(input('>'))
	
	if guess < secret_nr:
		speak('too low')
	elif guess > secret_nr:
		speak('too high')
	else:
		break #this is correct guess

if guess == secret_nr:
	speak('congrats, you got it in ' +str(guesses_taken) + ' guesses')
else:
	speak('wrong, the nr was ' +str(secret_nr))