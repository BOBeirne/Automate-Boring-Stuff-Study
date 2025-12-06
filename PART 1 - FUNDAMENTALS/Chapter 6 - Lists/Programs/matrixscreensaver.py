import random, sys, time

WIDTH = 70 #nr of columns

try:
	#for each column when counter == 0 no stream is shown
	#otherwise it acts as a counter for how many 0 or 1 should be displayed in column
	columns = [0] * WIDTH
	while True:
		for i in range(WIDTH):
			if random.random() < 0.02:
					# restarts stream counter on this column
					# stream length is 4-14 chars long
					columns[i] = random.randint(4,14)
			
			#print chars in this column
			if columns[i] == 0:
					#' ' is empty space
					print(' ',end='')
			else:
					#print 0 or 1
					print(random.choice([0, 1]), end='')
					columns[i] -= 1 #decrement counter
					
		print() #print newline at he end of row of columns
		time.sleep(0.1) #each row pauses for 0.1s
except KeyboardInterrupt:
	sys.exit() #end program using ctrl+C