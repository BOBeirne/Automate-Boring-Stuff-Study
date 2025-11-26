# Write a script that passes a submitted file to upload().
# Once the spreadsheet has uploaded to Google Sheets, download it using downloadAsExcel(), downloadAsODS(), 
# and other such functions to create a copy of the spreadsheet in these other formats.

import ezsheets

ss = ezsheets.upload('file_to_convert.xlsx') # upload 
ss.title = 'ConvertedSpreadsheet'
sheet = ss[0]

link = ss.url

uploaded_ss = ezsheets.Spreadsheet(link)

uploaded_ss.downloadAsExcel()
uploaded_ss.downloadAsODS()
uploaded_ss.downloadAsCSV()
uploaded_ss.downloadAsPDF()
uploaded_ss.downloadAsTSV()
uploaded_ss.downloadAsHTML()