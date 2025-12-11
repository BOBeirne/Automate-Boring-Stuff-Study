### Custom Invitations
#Say you have a text file of guest names. This guests.txt file has one name per line, as follows:
#Prof. Plum, Miss Scarlet, Col. Mustard, Al Sweigart and RoboCop

#Write a program that generates a Word document with custom invitations that look like Figure 17-10.
#Because Python-Docx can only use styles that already exist in a Word document, you’ll have to first add these styles to a blank Word file and then open that file with Python-Docx. 
#There should be one invitation per page in the resulting Word document, so call add_break() to add a page break after the last paragraph of each invitation. 
#This way, you will need to open only one Word document to print all of the invitations at once.

#You can download a sample guests.txt file from the book’s online resources.###

import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH 
from docx.enum.text import WD_BREAK


GUESTS_FILE =  'guests.txt'
DOCX_FILE = 'CustomInvitations.docx'
INVITATION_TEMPLATE = [
	("It would be a pleasure to have the company of", 'BODY'),
	("{guest_name}", 'GUEST'), # use placeholder for guest name
	("at 11010 Memory Lane on the evening of", 'BODY'),
	("April 1st", 'DATE'),
	("at 7 o'clock", 'BODY')
] # list of tuples: string, style type


### get the list of guests as a list ###
def get_guest_list(guests_file):
	guest_list = [] # initiate a list
	with open(guests_file) as file_obj:
		for line in file_obj:
			guest_list.append(line.strip().capitalize())
			#print(line) # test
	return guest_list

### Create the invitation ###
def create_invitation(TEMPLATE, guest_names):
	doc = docx.Document() # create a blank document
	for i, guest_name in enumerate(guest_names):# loop through guests
		for text, style_name in TEMPLATE: # loop through lines
			text_placeholder = text.replace('{guest_name}', guest_name) # replace the placeholder with actual guest name
			invite = doc.add_paragraph(text_placeholder) # add the line of text to the paragraph
			
			### Set up a general style for all paragraphs ###
			invite.alignment = WD_ALIGN_PARAGRAPH.CENTER # center align
			run = invite.runs[0] # get the run, make it center aligned
			run.font.name = 'Baguet Script Roman' # set the font to Baguet
			run.font.size = Pt(24) # set size to 24

			### Apply the style depending on the special type of paragraph###
			if style_name == 'GUEST':
				run = invite.runs[0]
				run.font.name = 'Calibri' # set style
				run.font.bold = True # make it bold
			elif style_name == 'DATE':
				run = invite.runs[0]
				run.font.name = 'Calibri' # set style
				run.font.bold = False # make it bold

		### Add page breaks ###
		if i < len(guest_names) - 1:
			doc.add_page_break() # add page break after each invitation except for the last one
	
	### Save the document ###
	doc.save(DOCX_FILE) # save the document
	print('Invitations generated successfully \n')

print('Starting to process guests invitations...')
guest_list = get_guest_list(GUESTS_FILE)
create_invitation(INVITATION_TEMPLATE, guest_list)