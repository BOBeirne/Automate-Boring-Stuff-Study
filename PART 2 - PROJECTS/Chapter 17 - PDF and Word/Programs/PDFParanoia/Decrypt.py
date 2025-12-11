#write a program that finds all encrypted PDFs in a folder (and its subfolders) and creates a decrypted copy of the PDF using a provided password. 
#If the password is incorrect, the program should print a message to the user and continue to the next PDF.

import os, pypdf, sys

try:
	### Get the password from CLI argument ###
	if len(sys.argv) != 2:
		print('Provide PDF password as a CLI argument when running this program')
		print('Expected usage: python Encrypt.py <password>')
		sys.exit()
	pdfpwd = sys.argv[1] # password is the CLI argument
	encrypted_pdfList = [] # list of encrypted pdf files

	### Walk the folder and subfolders looking for the pdf files###
	for folderName, subfolders, filenames in os.walk('.'): # check all folders and subfolders in cwd
		#print('The folder is:' + folderName) # testing
		#print('The subfolders in ' + folderName + ' are ' + str(subfolders)) # testing
		#print('The filenames in ' + folderName + ' are ' + str(filenames)) # testing
		
		### Find all ENCRYPTED pdfs, decrypt and rename them to _decrypted.pdf ###
		for file in filenames:
			if file.endswith('.pdf'): # find all pdf files not yet processed
				print(f'Processing {file} ...')
				source_path = os.path.join(folderName, file) # create a full path to the file
				reader = pypdf.PdfReader(source_path) # put the pdf into object
				if reader.is_encrypted == True: # check if it's encrypted
					encrypted_pdfList.append(source_path) # add it to the list
					print(f'{file} is encrypted, attempting to decrypt...')
					#reader.decrypt(pdfpwd) # commented out to avoid duplicate below
					#if reader.is_encrypted == False: # if file is now decrypted # this sometimes causes returning wrong result because of delay, the method below is faster
					if reader.decrypt(pdfpwd) != 0:
						print(f'Decryption of {file} confirmed as successful')
						writer = pypdf.PdfWriter() # create new empty pdf object
						#writer.append(reader) # copy encrypted file contents to the new pdf object # this does not work, using writer.append(reader) is unreliable for content modified in memory!!!
						for page in reader.pages: # this works, Must use a page-by-page loop to ensure the writer copies the content after it has been unlocked/decrypted in memory
							writer.add_page(page)
						with open( source_path + '_decrypted.pdf', 'wb') as file_obj:
							writer.write(file_obj) # save the new file
							print(f'Decrypted file saved as {file}_decrypted.pdf')
					else: # if file is not decrypted using provided password
						print(f'Decryption of {file} failed, checking next one...')
						pass
		print('*** Completed ***')

	if len(encrypted_pdfList) == 0:
		print('No encrypted PDFs found in this folder or subfolders')

except Exception as err:
	print(f'An exception occurred: {err}')