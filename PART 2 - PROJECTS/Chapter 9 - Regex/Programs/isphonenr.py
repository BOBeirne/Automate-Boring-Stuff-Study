def is_phone_nr(text):
	if len(text) != 12: #phone nrs have exactly 12 characters
		return False

	for i in range(0,3): # first 3 chars need to be int
		if not text[i].isdecimal():
			return False

	if text[3] != '-': # 4th char must be a dash
		return False

	for i in range(4,7): # next 3chars need to be nrs
		if not text[i].isdecimal():
			return False

	if text[7] != '-':
		return False

	for i in range(8,12): # next 4 chars need to be nrs
		if not text[i].isdecimal():
			return False

	return True


print(' is 415-555-4242 a phone nr?', is_phone_nr('415-555-4242'))
print(' is moshi moshi a phone nr?', is_phone_nr('moshi moshi'))

message = 'call me at 415-555-4242 tomorrow.'
for i in range(len(message)):
	segment = message[i:i+12]
	if is_phone_nr(segment):
		print('phone nr found: ' + segment)
print('done.')