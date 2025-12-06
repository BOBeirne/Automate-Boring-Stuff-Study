#Comma code FUNCTION

spam = ['apples', 'bananas', 'tofu', 'cats']

#print(str(spam[0:-1]) + ' and ' + str(spam[-1]))


def format_using_and(list):
	if not list: # empty list
		return ''
	elif len(list) == 1:
		return str(list[0])
	elif len(list) == 2:
		return str(list[0] + 'and ' + list[1])
	else: #all other scenarios
		more_than_two = ', '.join(str(list) for list in list[:-1])
		
		return more_than_two + ', and ' + str(list[-1])
	
print(format_using_and(spam))