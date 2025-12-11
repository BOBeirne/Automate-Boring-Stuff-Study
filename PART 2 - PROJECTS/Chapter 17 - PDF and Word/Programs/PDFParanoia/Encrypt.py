#Using the os.walk() function from Chapter 11, write a script that will go through every PDF in a folder (and its subfolders) 
#and encrypt the PDFs using a password provided on the command line. 

#Save each encrypted PDF with an _encrypted.pdf suffix added to the original filename. 
#Before deleting the original file, have the program attempt to read and decrypt the new file to ensure that it was encrypted correctly.

import os, pypdf, sys

try:
	### Get the CLI argument ###
	if len(sys.argv) != 2:
		print('Provide intended PDF password as a CLI argument when running this program')
		print('Expected usage: python Encrypt.py <password>')
		sys.exit()
	pdfpwd = sys.argv[1] # password is the CLI argument
	
	pdfList = [] # list of pdf files

	### Walk the folder and subfolders looking for the pdf files###
	for folderName, subfolders, filenames in os.walk('.'): # check all folders and subfolders in cwd
		print('The folder is:' + folderName) # testing
		print('The subfolders in ' + folderName + ' are ' + str(subfolders)) # testing
		print('The filenames in ' + folderName + ' are ' + str(filenames)) # testing

		### Find all pdfs, encrypt and rename them to _encrypted.pdf ###
		for file in filenames:
			if file.endswith('.pdf'): # find all pdf files not yet processed
				pdfList.append(file)

				### encrypt the new pdf###
				writer = pypdf.PdfWriter()
				writer.append(file) # copy file to a new writer object
				writer.encrypt(pdfpwd) # encrypt the file with pwd provided
				with open(file + '_encrypted.pdf', 'wb') as file_obj:
					writer.write(file_obj)
				print(f'Encrypted {file} to {file}_encrypted.pdf')

				### confirm if encryption was successful###
				reader = pypdf.PdfReader(file + '_encrypted.pdf')
				if reader.is_encrypted == True:
					print('Encryption of {file}_encrypted.pdf confirmed as successful, attempting to decrypt...')

					### Test the password###
					reader.decrypt(pdfpwd) # decrypt using pwd
					if reader.is_encrypted == False: # if file is now decrypted
						print(f'Decryption of {file}_encrypted.pdf confirmed as successful')
					else:
						print(f'Decryption of {file}_encrypted.pdf failed')

	if len(pdfList) == 0:
		print('No PDFs found in this folder or subfolders')
	else:
		for file in pdfList:
			os.unlink(file)
			print(f'file {file} has been deleted')

except Exception as err:
	print(f'An exception occurred: {err}')