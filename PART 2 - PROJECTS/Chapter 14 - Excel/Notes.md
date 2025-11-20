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

- You can check the **size** of the sheet with `Worksheet object`'s `max_row` and `max_column` attributes
- `max_column` will return and `integer` value instead of a letter of the column

```python
import openpyxl
wb = openpyxl.load_workbook('example3.xlsx') # load workbook from file example3.xlsx
sheet = wb['Sheet1'] # get the sheet named 'Sheet1' from a  workbook object
print(sheet.max_row) 
# 7
print(sheet.max_column) 
# 3
```

### Converting between column letters and numbers

- You can use `openpyxl.utils.get_column_letter()` function to convert from column number to column letter
- Use `openpyxl.utils.column_index_from_string()` function to convert from column letter to column number

```python
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

print(get_column_letter(1))
# 'A'
print(get_column_letter(2))
# 'B'
print(get_column_letter(27))
# 'AA'
print(get_column_letter(900))
# 'AHP'
print(column_index_from_string('A')) # Get 'A''s column number
# 1
print(column_index_from_string('AA')) # Get 'AA''s column number
# 27

wb = openpyxl.load_workbook('example3.xlsx')
sheet = wb['Sheet1']
get_column_letter(sheet.max_column)
# 'C'
```

### Getting rows and columns

- You can **slice** `worksheet object` to get all `cell objects` in a row, column or rectangle of cells.
	- You can loop over the cells in the slice
	- The slice of `cell objects` contains a **tuple** of `cell objects`

- In this example slice `['A1':'C3']` :
	- **cell object tuple** contains **3 **tuples**** - one for each **row**
	- **Each row tuple** contains **all cell objects** in the row 

```python
import openpyxl
wb = openpyxl.load_workbook('example3.xlsx') # load workbook from file example3.xlsx
sheet = wb['Sheet1'] # get the sheet named 'Sheet1' from a  workbook object

sheet['A1':'C3'] # Get cells from A1 to C3
# ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>), (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>), (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))

for row_of_cell_objects in sheet['A1':'C3']:
	for cell_object in row_of_cell_objects:
		print(cell_object.coordinate, cell_object.value)
	print('--- End of row ---')
"""
A1 2035-04-05 13:34:02
B1 Apples
C1 73
--- END OF ROW ---
A2 2035-04-05 03:41:23
B2 Cherries
C2 85
--- END OF ROW ---
A3 2035-04-06 12:46:51
B3 Pears
C3 14
--- END OF ROW ---
"""
```

- To access **values** of cells in a particular row or column, you can use `Worksheet object`'s `.rows` and `.columns` attributes
	- They need to be first converted to a list using `list()` function
	- this is a list of **tuples**, so you can use `index` to get the value of the cell
		- Each of these **tuples** represents a row and contains the `Cell objects` in that row
		- If we pass `columns` attribute to a `list()` will also give a list of tuples, one for cells in each column
	 - To access one particular tuple, you can refer to it by its **index in the larger tuple**. 
	 	 - For example: 
	 		- to get the tuple that represents column B, you’d use list(sheet.columns)[1]
			- To get the tuple containing the Cell objects in column A, you’d use list(sheet.columns)[0]

```python
import openpyxl
wb = openpyxl.load_workbook('example3.xlsx') # load workbook from file example3.xlsx
sheet = wb['Sheet1'] # get the sheet named 'Sheet1' from a  workbook object
print(list(sheet.columns)[1]) # get second column's cells as a list
#(<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>)

for cell_object in list(sheet.columns)[1]:
	print(cell_object.value)
"""
Apples
Cherries
Pears
Oranges
Apples
Bananas
Strawberries
"""
```

### Summary:

1.  Import the `openpyxl` module.
2.  Call the `openpyxl.load_workbook()` function to get a Workbook object.
3.  Use the `active` or `sheetnames` attribute.
4.  Get a `Worksheet object`.
5.  Use `indexing` or the `cell()` sheet method with `.rows` and `.columns` keyword arguments.
6.  Get a `Cell object`.
7.  Read the `Cell` object’s `.value` attribute.
## Creating and saving Excel Files

- `openpyxl` module allows you to create and save Excel files
- use `title` to modify the title of the sheet
- Anytime you modify the `Workbook object` or its `sheets` and `cells`, the spreadsheet file will **not be saved** until you call the `save()` workbook method

```python
import openpyxl
wb = openpyxl.Workbook() # create a Workbook object
print(wb.sheetnames) # Workbook starts with one sheet
# ['Sheet']
sheet = wb.active # get the active sheet
print(sheet.title) # get the title of the active sheet
# 'Sheet'
sheet.title = 'Spam Bacon Eggs Sheet' #  change the title of the sheet
print(wb.sheetnames) # get the names of all the sheets in the workbook
# ['Spam Bacon Eggs Sheet']

sheet.title = 'spam spam spam' # change the title of the sheet again
print(wb.sheetnames)

wb.save('example3_copy.xlsx') # save the workbook as example3_copy.xlsx
```

### Create and Remove sheets

- use `create_sheet()` method to create sheets
	- it returns a new `worksheet object` named `SheetX`, 
	- `SheetX` object is **by default the last sheet* in the workbook
	- You can specify index and title of the sheet passing it arg:
		- `index=` to specify index location
		- `title=' '`to specify the title of the sheet
- use `del` operator to remove sheets, for eg. `del wb['Sheet']`

```python
import opennpyxl
wb = openpyxl.Workbook() # create a Workbook object in wb variable
wb.sheetnames 
# ['Sheet']

wb.create_sheet() # create a new sheet 
# <Worksheet "Sheet1">
wb.sheetnames # get the list of sheetnames 
# ['Sheet', 'Sheet1'] 

wb.create_sheet(index=0, title='First Sheet') #  create new sheet at the index id=0 called First Sheet
wb.sheetnames # get the list of sheetnames 
# ['First Sheet', 'Sheet', 'Sheet1']

wb.create_sheet(index=2, title='Middle Sheet') #  create new sheet at the index id=2 called Middle Sheet
# <Worksheet "Middle Sheet">

wb.sheetnames
# ['First Sheet', 'Sheet', 'Middle Sheet', 'Sheet1']

del wb['Middle Sheet']
del wb['Sheet']
wb.sheetnames
# ['First Sheet', 'Sheet']
```

### Writing values to cells

- Very **similar to writing values to keys in a Dictionary**

```python
import openpyxl
wb =openpyxl.Workbook()

sheet = wb['Sheet'] #  specify the sheet to work on

sheet['A1'] = 'Hello, World!' # edit the A1 cell's value
print(sheet['A1'].value) # 'Hello, world!'
```

### Font Style of Cells

- You can change formatting inside cells to highlight important areas
- to do that you need to use the `Font()` 
	- it needs to be imported using `from openpyxl.styles import Font`
	- Use `size=` to change the font size
	- To change font type to bold/italic/underscore etc assign them `True` value, more in the table below:

| Keyword Argument | Data Type | Description |
| :--- | :--- | :--- |
| **name** | String | The font name, such as 'Calibri' or 'Times New Roman'. |
| **size** | Integer | The point size of the font. |
| **bold** | Boolean | Set to `True` for bold font styling. |
| **italic** | Boolean | Set to `True` for italic font styling. |


```python
import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook() # Create new workbook object
sheet = wb['Sheet'] # select the sheet

italic_24_font = Font(size=24, italic=True) # store Font object in the variable

sheet['A1'].font = italic_24_font
sheet['A1'] = 'Hello, world!'
wb.save('styles3.xlsx')
```

- You can call `Font()` to create a `Font object` and store that Font object in a variable. You then assign that `.font` variable to a `Cell object’s` font `attribute`

```python
import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook() # Create new workbook object
sheet = wb['Sheet'] # select the sheet

bold_font = Font(name='Times New Roman', bold=True) # store TNR styled, bold Font object in the variable

sheet['A1'].font = bold_font
sheet['A1'] = 'Bold times new roman'

italic_24_font = Font(size=24, italic=True) # store Font object in the variable

sheet['B3'].font = italic_24_font
sheet['B3'] = '24 pt Italic`

wb.save('styles3.xlsx')
```

### Formulas

- Formulas start with `=` sign, you can add them to the cells
- The `openpyxl module` **can't calculate Excel formulas** and populate cells with the results.
	- If you open this `writeFormula3.xlsx` file in Excel, Excel itself will populate the cells with the formula results.
	- to see **only** calculation results you can use `data_only=true` when using `openpyxl.load_workbook()` and cell values should show as a **calculated result**

```python
import openpyxl
wb = openpyxl.Workbook() # Create new workbook object
sheet = wb['Sheet'] # select the sheet

sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)' # set the formula
wb.save('writeFormula3.xlsx')

wb.active['A3'].value  # Get the formula string.
# '=SUM(A1:A2)'
wb = openpyxl.load_workbook('writeFormula3.xlsx', data_only=True)  # Open with data_only.
wb.active['A3'].value  # Get the formula result only
# 500
```

### Adjusting Rows Height and Columns Width

- You can adjust the size of rows and columns using `row_dimensions` and `column_dimensions` attributes in `Worksheet object`

```python
import openpyxl
wb = openpyxl.Workbook() # Create new workbook object
sheet = wb['Sheet'] # select the sheet

sheet['A1'] = 'Tall Row'
sheet['B2'] = 'Wide Column'

sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20

wb.save('dimensions3.xlsx')
```

### Merging and un-merging cells

- You can merge cells using `merge_cells()` and `unmerge_cells()`
- To merge cells, you need to pass the **top_left_cell** and **bottom_right_cell** parameters to the `merge_cells()` method

```python
import openpyxl
wb = openpyxl.Workbook() # Create new workbook object
sheet = wb['Sheet'] # select the sheet

sheet.merge_cells('A1:D3') # Merge all these cells.
sheet['A1'] = 'Twelve cells merged together.'
sheet.merge_cells('C5:D5') # Merge these two cells.
sheet['C5'] = 'Two merged cells.'
wb.save('merged3.xlsx')

sheet.unmerge_cells('A1:D3') # Split these cells up.
sheet.unmerge_cells('C5:D5') # Split these cells up.
wb.save('unmerged3.xlsx')
```

### Freezing Panes

- Sometimes it's helpful to **"freeze"** the top row and left column of a spreadsheet, so that the user doesn't have to scroll around to see the data, they are called **Freeze Panes**
- This attribute will **freeze all rows above this cell and all columns to the left of it**, but **not the row and column of the cell itself**
- To **unfreeze** all panes, set `freeze _panes` to `None` or `'A1'`

| Setting Input | Frozen Rows | Frozen Columns |
| :--- | :--- | :--- | 
| **`sheet.freeze_panes = 'A2'`** | Row 1 | None | 
| **`sheet.freeze_panes = 'B1'`** | None | Column A | 
| **`sheet.freeze_panes = 'C1'`** | None | Columns A and B |
| **`sheet.freeze_panes = 'C2'`** | Row 1 | Columns A and B | 
| **`sheet.freeze_panes = 'A1'`** or **`sheet.freeze_panes = None`** | None | None |

```python
import openpyxl
wb = openpyxl.Workbook() # Create new workbook object
sheet = wb['Sheet'] # select the sheet

sheet.freeze_panes = 'A2' # Freeze the rows above A2
wb.save('freezeExample3.xlsx')
```

### Charts

- You can make charts using `openpyxl.chart` module

1) Create a `Reference object` from **rectangular section of cells**
2) Create a `Series object` by passing in `Reference object`
3) Create `Chart object`
4) Append `Series object` to `Chart object`
5) Add the `Chart object` to the `Worksheet object`, optionally specyfying which **cell** should be **top-left** corner of the chart

#### Reference object

- To create `Reference objects`, you must call the `openpyxl.chart.Reference()` function and pass **five arguments**:
	1) `Worksheet object`
	2) `Column` and `Row` **Integer** of the **top-left cell** of the selection (tuple = row, column)
	3) `Column` and `Row` **Integer** of the **bottom-right cell** of the selection (tuple = row, column)

```python
import openpyxl
wb = openpyxl.Workbook() # Create new workbook object
sheet = wb.active

for i in range(1,11): # create some data in col A
	sheet['A' + str(i)] = i * i

ref_obj = openpyxl.chart.Reference(sheet, 1, 1, 1, 10) # pass the 5 arguments

series_obj = openpyxl.chart.Series(ref_obj, title='first series') # create a series object
chart_obj = openpyxl.chart.BarChart() # create a chart object in BarChart type
chart_obj.title = 'My chart'
chart_obj.append(series_obj) # append the series object to the chart object

sheet.add_chart(chart_obj, 'C5') # add the chart object to the sheet at the location C5

wb.save('chartExample3.xlsx')
```

