"""
Download the ZIP file excelSpreadsheets.zip from the book’s online resources 
and unzip the spreadsheets into the same directory as your program. <--- that zip is full of csv files???

create one CSV file per sheet. 
The filenames of the CSV files should be 
<excel filename>_<sheet title>.csv, 
where <excel filename> is the filename of the Excel file without the file extension 
(for example, spam_data, not spam_data.xlsx) 
and <sheet title> is the string from the Worksheet object’s title variable.
"""

import os, openpyxl, csv


for file in os.listdir('.'):
#	# Skip non-xlsx files,
#	if not file.endswith('.xlsx'): 
#		print(f'Skipping file {file}, not an Excel file...')
#		continue

	# If file is an Excel file
	if file.endswith('.xlsx'):
		print(f'Processing file {file} ...')
		excel_file = file[:-len('.xlsx')] # Clear up the .xlsx extension from file name
		wb = openpyxl.load_workbook(file) # load the workbook object
		
		# Loop through every sheet in the workbook.
		for sheet_name in wb.sheetnames:
			sheet = wb[sheet_name]
			csv_filename = str(excel_file) + '_' + str(sheet_name) + '.csv' # Create the CSV filename from the Excel filename and sheet title.
			# Create the csv.writer object for this CSV file.
			output_file = open(csv_filename, 'w', newline='')
			csv_writer = csv.writer(output_file)
			#print(f'Processing sheet: {sheet_name}')

			# Loop through every row in the sheet.
			for row in range(1, sheet.max_row + 1):
				#print(f'Processing row: {row}')
				row_data = []
				#row_data.append(row) # Append each cell to this list.

				# Loop through each cell in the row.
				for col_num in range(1, sheet.max_column + 1):
					print(f'Processing column: {col_num}')
					cell_data = sheet.cell(row=row, column=col_num).value # get the value of the cell
					row_data.append(cell_data) # Append each cell's data to row_data
				# Write the row_data list to the CSV file.
				csv_writer.writerow(row_data)
				print(f'wrote row data to file {csv_filename}')
			output_file.close()
			print(f'Completed processing file {file}, new file saved as {csv_filename}')