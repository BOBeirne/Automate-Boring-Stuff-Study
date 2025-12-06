'''
paste text from the clipboard
do something to it (add * as bullet points)
copy new text to clipboard

text for copying:

Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''



import pyperclip
text = pyperclip.paste()
lines = text.split('\n') #separate lines

for i in range(len(lines)): #loop though all indexes in the 'lines' list
	lines[i] = '*' + lines[i] #add stars hereat the beginning of each index in 'lines'

text = '\n'.join(lines) #join lines back again
pyperclip.copy(text)

print(pyperclip.paste())