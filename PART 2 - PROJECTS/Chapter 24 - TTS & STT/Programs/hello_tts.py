'''
I ran into issues with this code as program would not speak the 2nd line. 
It looks like it is not releasing the engine and the only way to stop the engine is to use function wrapper.
This is apparently a quite common issue with this module

---
import pyttsx3, time

engine = pyttsx3.init()
engine.say('Hello, How are you doing today?')
engine.runAndWait() # # speak and wait
time.sleep(1) # running into issues here
feeling = input('>') # for the user to input how they are feeling

engine.say('Yes. I am feeling ' + feeling + ' as well.')
engine.runAndWait()
print(engine.getProperty('voice')) '''


import pyttsx3

def speak(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.startLoop(False)
	engine.iterate()
	while engine.isBusy():
		engine.iterate()
	engine.endLoop()

speak('Hello, How are you doing today?')
feeling = input('>')
speak('Yes. I am feeling ' + feeling + ' as well.')