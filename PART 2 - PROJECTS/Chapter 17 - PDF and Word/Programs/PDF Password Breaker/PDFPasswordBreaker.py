# Say you have an encrypted PDF that you’ve forgotten the password to, but you remember it was a single English word. 
#Trying to guess your forgotten password is quite a boring task. 

#Instead, you can write a program that will decrypt the PDF by trying every possible English word until it finds one that works. 
#This is called a brute-force password attack. Download the text file dictionary.txt from the book’s online resources. 
#This dictionary file contains over 44,000 English words, with one word per line.

#Using the file-reading skills you learned in Chapter 10, create a list of word strings by reading this file. 
#Then, loop over each word in this list, passing it to the decrypt() method. 
#You should try both the uppercase and lowercase forms of each word. 

#(On my laptop, going through all 88,000 uppercase and lowercase words from the dictionary file takes a couple of minutes. 
#This is why you shouldn’t use a simple English word for your passwords.)

import pypdf

DICTIONARY_FILE = 'dictionary.txt'
PDF_FILE = 'encrypted.pdf' # pw is 'swordfish', which turns out it not in the dictionary file... thanks Al...


def check_file_validity(pdffile): # pass the dictionary and encrypted file to the program

	# First check if there is file to encrypt#
	try:
		reader = pypdf.PdfReader(pdffile) # create pdf reader object to work on
	except FileNotFoundError:
		print('File not found')
		return
	if not reader.is_encrypted:
		print('File is not encrypted')
		return
	else:
		return reader

def find_password(reader, dictionary):
	# Run the dictionary check loop
	print('*** Starting ***')
	try:
		with open (dictionary, 'r') as file_obj: # open up the dictionary in read mode
			for word in file_obj: # cycle through each line (word) in dictionary
				word = word.strip() # strip each word just in case there are newlines
				print(f'trying {word}')

				if reader.decrypt(word.lower()) != 0: # try out the lowercase version of the word
					print(f'The correct password is {word}')
					break # stop if successful


				elif reader.decrypt(word.upper()) != 0: # try out the uppercase version of the word
					print(f'The correct password is {word}')
					break # stop if successful

	except FileNotFoundError:
		print('File not found')
	print('*** Completed ***')

if __name__ == "__main__":
	# Check if file is valid
	reader_obj = check_file_validity(PDF_FILE)
	# Run the check if file is valid
	if reader_obj:
		find_password(reader_obj, DICTIONARY_FILE)
