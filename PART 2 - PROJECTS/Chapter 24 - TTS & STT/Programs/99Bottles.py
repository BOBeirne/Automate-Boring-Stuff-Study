"""
Singing “99 Bottles of Beer”
Cumulative songs are songs whose verses repeat with additions or slight changes. 
The songs “99 Bottles of Beer” and “The 12 Days of Christmas” are examples of cumulative songs. 
Write a program that sings (or at least speaks) the lyrics in “99 Bottles of Beer”:

99 bottles of beer on the wall,
99 bottles of beer,
Take one down, pass it around,
98 bottles of beer on the wall.

These lyrics repeat, with one fewer bottle each time. 
The song continues until it reaches zero bottles, at which point the last line is “No more bottles of beer on the wall.” 
(You may wish to have the program start at 2 or 3 instead of 99 to make testing easier.)
"""
import sys, time, pyttsx3

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

i = 10
while True:
	if i > 0:
		speak(f'{i} Bottles of beer on the wall')
		speak('Take one down, pass it around,')
		i -= 1
		time.sleep(0.5)
	else:
		speak('No more bottles of beer on the wall.')
		sys.exit()