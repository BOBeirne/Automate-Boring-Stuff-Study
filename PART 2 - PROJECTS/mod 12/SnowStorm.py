# Text-based snowstorm animation

import os, random, sys, time

TOP = chr(9600)
BOTTOM = chr(9604)
FULL = chr(9608)

# set the snowstorm density to the command line argument:
DENSITY = 4 # Default snow density is 4%

if len(sys.argv) > 1:
	DENSITY = int(sys.argv[1]) # set density as length of 1st arg

def clear():
	os.system('cls if os.name == "nt" else clear')

while True:
	clear() #clear the terminal
	for y in range(20): # loop over each row and column
		for x in range(40):
			if random.randint(0,99):
				print(random.choice([TOP, BOTTOM]), end='') #print snow
			else:
				print(' ', end='') # print empty space
		print() # newline
	print(FULL *40 + '\n' + FULL * 40)
	print('(Ctrl+C to stop)')
	time.sleep(0.2) #pause