# Simple stopwatch program

import time
import pyperclip

# Display instructions
print('Press ENTER to begin Stopwatch and to mark each lap. Press CTL+C to quit')
input() # Wait for ENTER
print('Starting...')

startTime = time.time()
lastTime = startTime
lapNr = 1 # Intitiate counter
Summary = []

# Tracking lap times
try:
	while True:
		input() # accepts any ENTER input
		lapTime = round(time.time() - lastTime, 2) # round the result of lap time to 2 decimal points
		totalTime = round(time.time() - startTime, 2) # cal the total to 2 decimal points
		LapTxt = f'Lap #{str(lapNr).rjust(2)}: {str(totalTime).rjust(4)} ({str(lapTime).rjust(2)})'
		print(LapTxt)
		Summary.append(LapTxt)
		lapNr += 1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	# Handle CTRL+C to stop the program nicely
	FinalTxt = f'Done, total laps: {lapNr}, total time: {totalTime} s'
	print(FinalTxt)
	Summary.append(FinalTxt)
	pyperclip.copy('\n'.join(Summary)) # This copies whole list of all laps and final summary to the clipboard as a single str with newlines to separate them
	print('Results copied to the clipboard.')
except Exception as err:
		print(f'An error occurred: {err}')