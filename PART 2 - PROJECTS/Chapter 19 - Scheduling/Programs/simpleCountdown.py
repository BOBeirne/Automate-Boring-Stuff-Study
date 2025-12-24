# Simple countdown script

import time as t
import subprocess

timeLeft = 60

# count down 60s
while timeLeft > 0:
	print(timeLeft)
	time.sleep(1)
	timeLeft -= 1

# At the end of countdown play .wav file
print("Time's up!")
subprocess.run(['start', 'alarm.wav'], shell=True) # Windows
#subprocess.run(['open', 'alarm.wav'])  # macOS and Linux

# You can also create a popup message instead of playing a sound