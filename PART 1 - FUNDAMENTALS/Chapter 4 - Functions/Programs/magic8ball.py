import random

def get_answer(answ_nr):
	# returns fortune answ based on what int answer_nr is 1-9
	if answ_nr == 1:
		return 'it is certain'
	elif answ_nr == 2:
		return 'It is decidedly so'
	elif answ_nr == 3:
		return 'yes'
	elif answ_nr == 4:
		return 'try again'
	elif answ_nr == 5:
		return 'ask later'
	elif answ_nr == 6:
		return 'try asking again later'
	elif answ_nr == 7:
		return 'no'
	elif answ_nr == 8:
		return 'not good'
	elif answ_nr == 9:
		return 'doubtful'
	
print(' ask yes/no question')
input('>')
'''this whole block can be merged into one:
r = random.randint(1,9)
fortune = (get_answer(r))
print(fortune)'''

print(get_answer(random.randint(1,9)))