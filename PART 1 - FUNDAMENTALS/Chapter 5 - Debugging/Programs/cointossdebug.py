import random

def toss():
	if random.randint(0, 1) == 1: # 0 is tails 1 is heads
		return 'heads'
	else:
		return 'tails'
		
		
guess = ''
while guess not in ('heads', 'tails'):
	print('guess the coin toss - heads or tails, you get 2 guesses')
	guess = input('').lower()
	
	
toss_result = toss()    
if toss_result == guess:
	print('you got it')
else:
	print('guess again')
	guess = input().lower()
	if toss_result == guess:
		print('congrats')
	else:
		print('you''re really bad at this...')