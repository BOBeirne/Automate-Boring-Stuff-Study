""" This program is a function that returns the text from a .docx file, you can call it like a module"""

import docx

def get_text(filename): # use the function call
	doc = docx.Document(filename) # pass the filename name in cwd
	full_text = [] # initiate empty list for the full text string
	for paragraph in doc.paragraphs: # loop over paragraphs
		full_text.append(paragraph.text) # add each paragraph to the list
	return '\n'.join(full_text) # return full text with each paragraph in new line