# this program takes 2 integers = N and M as an extra CLI arguments
# starting at row N it should insert an M number of blank rows into the spreadsheet

# will be working on the multiplicationTable.xlsx spreadsheet and save a copy as it can generate a large nrs of rows quickly

import openpyxl, sys

wb = openpyxl.load_workbook('multiplicationTable.xlsx')
sheet = wb.active

if len(sys.argv) > 2: # if there are at least 2 command line arguments passed when running the program
	N = sys.argv[1] # get the N number from the command line first extra argument
	M = sys.argv[2] # get the M number from the command line second extra argument
else:
	print('Program needs to be run from CLI and requires 2 extra integer arguments. Please enter 2 numbers after the program name.')
	exit()

N = int(N)
M = int(M)
cells = list(sheet.rows)[N-1][:M] # get the M cells from row N 

for cell in cells:
	sheet.insert_rows(N) # insert a blank row at row N

wb.save('multiplicationTable_copy.xlsx')