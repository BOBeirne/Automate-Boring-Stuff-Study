'''
def spam(divide_by):
	try: #any code in his block that causes zerodivisionerror wont crash the program
		return 42 / divide_by
	except ZeroDivisionError:
		# if ZeroDivisionError
		print('Error, invalid arg')
print (spam(2))
print (spam(12))
print (spam(0))
print (spam(1))
print (spam())
'''
#version where the try is called in spam() block

def spam(divide_by):
	return 42 / divide_by
	
try:
	print (spam(2))
	print (spam(12))
	print (spam(0))
	print (spam(1))

except ZeroDivisionError:
# if ZeroDivisionError
	print('Error, invalid arg')