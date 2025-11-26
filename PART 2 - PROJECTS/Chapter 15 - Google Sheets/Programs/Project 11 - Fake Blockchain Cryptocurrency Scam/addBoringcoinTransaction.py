# program adds a row to the end of the Google Sheets for a new transaction
# It reads three command line arguments from the list in sys.argv: the sender, the recipient, and the amount.

import sys, ezsheets

if len(sys.argv) < 4:
	print('Provide 3 arguments: sender recipient amount')
	sys.exit()

sender, recipient, amount = sys.argv[1:] # unpack CLI arguments into variables
# no need to convert str to integer as it will be saved into spreadsheet

# connect to the Sheet containing "blockchain" and select first sheet
ss = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1m7bUWdbX5QhmBIsVCb1LVcNd55Vi1ea7/edit?gid=1849041866') # personal copy
sheet = ss.sheets[0]

sheet.rowCount += 1 # add new row for new transaction
sheet[1, sheet.rowCount] = sender
sheet[2, sheet.rowCount] = recipient
sheet[3, sheet.rowCount] = amount
