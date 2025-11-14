# Excel spreadsheets


## Openpyxl module

- [Documentation](https://openpyxl.readthedocs.io/en/stable/)
- [Excersise materials](https://nostarch.com/automate-boring-stuff-python-3rd-edition)
- `openpyxl` module allows to read and modify excel spreadsheets
- needs to be installed: `pip install openpyxl`
- Works with **MS Excel** and **LibreOffice Calc**
	- files need to be closed prior to modification using Python `openpyxl` module.
	- if using O365, you need to download the file to local machine and then after making changes, reupload back to Office365.

### Reading Excel Files

- Excel spreadsheet is referred to as `workbook` and is saved ina  file with `.xlsx` extension
	- Currently viewed (or last viewed before closing) worksheet is called **active (work)sheet**
	- Each `workbook` contains one or more `worksheets` (sheets) 
		- Each `cheet` has `columns` (addressed by letters starting from A)
		- And `rows` (addressed by numbers starting from 1)
		- `box` at a particular columnn is called `cell`
			- each `cell` can contain one or more `values

```python
import openpyxl
wb = openpyxl.load_workbook('example3.xlsx') # load workbook from file example3.xlsx
type(wb) # <class 'openpyxl.workbook.workbook.Workbook'>
```

### Getting Sheets from the Workbook

- You can use `sheetnames` attribute to get the names of the sheets in the workbook

```python
import openpyxl
wb = openpyxl.load_workbook('example3.xlsx') # load workbook from file example3.xlsx
print(wb.sheetnames) # ['Sheet1', 'Sheet2', 'Sheet3']
sheet = wb['Sheet3'] # get the sheet named 'Sheet3'
print(sheet) # <Worksheet "Sheet3"> 
type(sheet) # <class 'openpyxl.worksheet.worksheet.Worksheet'>
sheet.title # 'Sheet3' # get the title of the sheet
another_sheet = wb.active # get the active sheet
print(another_sheet) # <Worksheet "Sheet1">
```

- **Each sheet** is represented by `Worksheet object`, which you can get by using square brackets with the sheet name string (just like dictionary keys)
- You can use `active` attribute of a `Workbook object` to get the active sheet

### Getting Cells from a Sheets

- Once you have `worksheet object`, you can use `cell` attribute to get the cell object by it's name
- `cell object` has `value` attribute inside the cell
- Calling `value` attribute on the `cell object` returns the value of the cell

- For example: 
	- Accessing `value` attribute of `cell object` for cell `B1` will return str 'apples'
	- `row` attribute of `cell object` for cell `B1` will return int 1
	- `column` attribute of `cell object` for cell `B1` will return int 2
	- `coordinate` attribute of `cell object` for cell `B1` will return str 'B1'

```python
import openpyxl
wb = openpyxl.load_workbook('example3.xlsx') # load workbook from file example3.xlsx
sheet = wb['Sheet1'] # get the sheet named 'Sheet1' from a  workbook object
print(sheet['A1']) # <Cell 'Sheet1'.A1>
print(sheet['A1'].value) # datetime.datetime(2035, 4, 5, 13, 34, 2)
c = sheet['B1']
print(c.value) # 'Apples'
print(f'Row {c.row}, Column {c.column} is {c.value}') # 'Row 1, Column 2 is Apples'
print(f'''Cell {c.coordinate} is {c.value}''') # 'Cell B1 is Apples'
print(sheet['C1'].value) # 73
```

- **dates** are automatically converted to `datetime` objects by `openpyxl` module (more in [[Chapter 19]])

- **Letters** can be tricky to program, because after column 'Z' they start using 2 letters ('AA', 'AB', 'AC' etc)
	- You can use sheet's `cell() method` to get a `cell object` by it's coordinates (row, column)
	- They start from integer 1 for `row` and integer 1 for `column` (**not 0**)

```python
import openpyxl
wb = openpyxl.load_workbook('example3.xlsx') # load workbook from file example3.xlsx
sheet = wb['Sheet1'] # get the sheet named 'Sheet1' from a  workbook object
print(sheet.cell(row=1, column=2)) # <Cell 'Sheet1'.B1>
print(sheet.cell(row=1, column=2).value) # 'Apples'

for i in range (1, 8, 2): # Go through every other row
	print(i, sheet.cell(row=i, column=2).value) # print the nr of the row and the value of the cell
# 1 Apples
# 3 Pears
# 5 Apples
# 7 Strawberries
```

- You can check the size of the sheet with `Worksheet object`'s `max_row` and `max_column` attributes

```python
import openpyxl
wb = openpyxl.load_workbook('example3.xlsx') # load workbook from file example3.xlsx
sheet = wb['Sheet1'] # get the sheet named 'Sheet1' from a  workbook object
print(sheet.max_row) 
# 7
print(sheet.max_column) 
# 3
```