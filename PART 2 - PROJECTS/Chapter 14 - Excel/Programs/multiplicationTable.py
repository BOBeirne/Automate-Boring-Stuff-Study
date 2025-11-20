# Takes a number N from the command line and creates an N×N multiplication table in an Excel spreadsheet. 
# for eg. if run using py multiplicationTable.py 6 it will create multiplication table up until nr 6x6
# Row 1 and column A should contain labels and be in bold.

import openpyxl, sys
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.active

bold_cell = Font(bold=True)

if len(sys.argv) > 1: # if there is a command line argument passed when running the program
	N = sys.argv[1] # get the number from the command line
else:
	print('Program needs to be run from CLI. Please enter a number after the program name.')
	exit()

N = int(N)

for row in range(1, N+1): # iterate through the rows starting from row 2 and ending at row N
	for col in range(1, N+1): # iterate through the columns starting from column 2 and ending at column N
		cell = sheet.cell(row=row, column=col)
		cell.value = row * col


for row_cell in list(sheet.rows)[0]: # get the first row and set the font to bold to all cells in that row
	row_cell.font = bold_cell

for column_cell in list(sheet.columns)[0]: # get the first column and set the font to bold to all cells in that column
	column_cell.font = bold_cell

wb.save('multiplicationTable.xlsx')