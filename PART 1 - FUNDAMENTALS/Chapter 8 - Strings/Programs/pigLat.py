# English to pig latin
print('enter message to translate into pig latin')
message = input('>')

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = [] # list of words in pig latin

for word in message.split():
	#separate non-letters at the start of this word:
	prefix_non_letters = ''
	while len(word) > 0 and not word[0].isalpha():
		prefix_non_letters += word[0]
		word = word[1:]
	if len(word) == 0:
		pig_latin.append(prefix_non_letters)
		continue
	
	# separate non-letters at the end of this word:
	suffix_non_letters = ''
	while not word[-1].isalpha():
		suffix_non_letters = word[-1] +  suffix_non_letters
		word = word[:-1]

	# remember if word was in uppercase or title:
	was_upper = word.isupper()
	was_title = word.istitle()

	word = word.lower() #  make it all lowercase for translation

	# Separate consonants at the start of this word:
	prefix_consonants = ''
	while len(word) > 0  and word[0] not in VOWELS:
		prefix_consonants += word[0]
		word = word[1:]

	# Add pig latin ending to the word:
	if prefix_consonants !='':
		word += prefix_consonants + 'ay'
	else:
		word += 'yay'
		
	# set word back to uppercase or title
	if was_upper:
		word = word.upper()
	if was_title:
		word = word.title()

	# Add non-letters back to the start or end of the word
	pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# join all words together into single string
print(' '.join(pig_latin))