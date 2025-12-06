birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
	name = input('Enter name: (blank to quit)')
	if name == '':
		break
	
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of '+ name)
	else:
		print('I dont have info about' + name)
		bday = input('whats their bd?')
		birthdays[name] = bday
		print('Bday database updated')
		
print(birthdays)