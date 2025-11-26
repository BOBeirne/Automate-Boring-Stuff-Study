# get spreadsheet - https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg
# check the totals mistake
# int(ss.sheets[0].getRow(2)[0]) * int(ss.sheets[0].getRow(2)[1]) == int(ss.sheets[0].getRow(2)[2]) == True if row 2 has the correct total.

import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

sheet = ss.sheets[0]

row_id = 0 # start at 0

for row_id in range(2, (sheet.rowCount + 1)): # skip first row - title
	row_data = sheet.getRow(row_id) # get each row data (list of strings)

	if not row_data[0] or not row_data[1] or not row_data[2]:
		continue

	first = int(row_data[0])
	second = int(row_data[1])
	total = int(row_data[2])

	if first * second != total:
		print(f'Error found at row {row_id}')