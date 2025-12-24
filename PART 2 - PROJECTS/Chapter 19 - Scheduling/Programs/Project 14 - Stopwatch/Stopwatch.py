# Simple stopwatch program

import time

# Display instructions
print('Press ENTER to begin Stopwatch and to mark each lap. Press CTL+C to quit')
input() # Wait for ENTER
print('Starting...')

startTime = time.time()
lastTime = startTime
lapNr = 1 # Intitiate counter

# Tracking lap times
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2) # round the result of lap time to 2 decimal points
		totalTime = round(time.time() - startTime, 2) # cal the total to 2 decimal points
		print(f'Lap #{lapNr}: {totalTime}({lapTime})', end='')
		lapNr += 1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	# Handle CTRL+C to stop the program nicely
	print(f'Done, total laps: {lapNr}, total time: {totalTime} s')