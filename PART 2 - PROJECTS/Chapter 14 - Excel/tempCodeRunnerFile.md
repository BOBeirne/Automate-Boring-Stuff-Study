import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook() # Create new workbook object
sheet = wb['Sheet'] # select the sheet

italic_24_font = Font(size=24, italic=True)

sheet['A1'].font = italic_24_font
sheet['A1'] = 'Hello, world!'
wb.save('styles3.xlsx')