# combine_pdfs.py - Combines all the PDFs in the current working directory
# into a single PDF file.

"""Step 1: Find All PDF Files"""
import pypdf, os

# Get all the PDF filenames:
pdf_filenames = [] # empty list
for filename in os.listdir('.'): # loop through all files in the current directory
	if filename.endswith('.pdf'):
		pdf_filenames.append(filename) # add anything ending with .pdf to the list
	
# sort the list of PDF filenames:
pdf_filenames.sort(key=str.lower) # sort the list alphabetically and lowercase all letters

writer = pypdf.PdfWriter() # create a PdfWriter object, a blank PDF

"""Step 2: Open Each PDF"""

# Loop through all PDFs
for pdf_filename in pdf_filenames: # loop through the list of PDF filenames
	reader = pypdf.PdfReader(pdf_filename) # open the PDF file

	# Copy all pages after the first page (skip the title page)
	writer.append(pdf_filename, (1, len(reader.pages)))

"""Step 3: Save the Results"""

# Save the resulting PDF to a file:
with open('combined.pdf', 'wb') as file:
	writer.write(file)