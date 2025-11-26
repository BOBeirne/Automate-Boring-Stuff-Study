# write a program that can automatically download the form information that users have submitted using Google Forms
# Slightly changing this program to get the answers from a form instead of email addresses (column B cells)

# 1) Create a Form and input some data
# 2) Extract data into sheets document - https://docs.google.com/spreadsheets/d/1tk37XOeLp0za2_Tm4qdGr-qZQnRGNFRryQejCKCMcL8/edit?usp=sharing
# 3) run this script

import ezsheets

ss = ezsheets.Spreadsheet('1tk37XOeLp0za2_Tm4qdGr-qZQnRGNFRryQejCKCMcL8') # Get the spreadsheet where the data is
sheet = ss.sheets[0] # Get the first sheet
list_of_answers = sheet.getColumn('B') # Get the second column values as a list

for cell in list_of_answers[1:]: # loop through the list of cell values
	print(cell)