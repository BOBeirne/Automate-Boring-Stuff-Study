# Practice Questions

## For the following questions, imagine you have a Workbook object in the variable `wb`, a `Worksheet object` in sheet, and a `Sheet object` in sheet.

1) What does the openpyxl.load_workbook() function return?

It returns a workbook object

2) What does the wb.sheetnames workbook attribute contain?

the name of all the sheets in the current workbook

3) How would you retrieve the Worksheet object for a sheet named 'Sheet1'?

put it in a variable `sheet = wb['Sheet1']`

4) How would you retrieve the Worksheet object for the workbook’s active sheet?

use active attribute `active_sheet = wb.active`

5) How would you retrieve the value in cell C5?

use `.value` on a cell object for eg. `sheet['A1'].value`

6) How would you set the value in cell C5 to "Hello"?

`sheet['C5'] = 'Hello'`

7) How would you retrieve the cell’s row and column as integers?

put cell object into variable 
`cell = sheet['F50']`
then call `.row` and `.column` attributes on the variable
`row = cell.row`
`column = cell.column`4

8) What do the sheet.max_column and sheet.max_row sheet attributes hold, and what is the data type of these attributes?

They return the size of the sheet in each direction
data type is `integer`

9) If you needed to get the integer index for column 'M', what function would you need to call?

use `openpyxl.utils.column_index_from_string()` 
You need to import it from `openpyxl.utils` first using `from openpyxl.utils import column_index_from_string`
and then call it using `column_index_from_string('M')`

10) If you needed to get the string name (Letter) for row 14, what function would you need to call?

use `openpyxl.utils.get_column_letter()` 
before that, import it - `from openpyxl.utils import get_column_letter`
and then call it using `get_column_letter(14)`


11) How can you retrieve a tuple of all the Cell objects from A1 to F1?

`sheet['A1':'F1']`

12) How would you save the workbook to the filename example3.xlsx?

`wb.save('example3.xlsx')`

13) How do you set a formula in a cell?

you add the formula to the cell object like this: `sheet['A3'] = '=SUM(A1:A2)'`

14) If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?

need to save the document first, then import it again but use `data_only=True` as an argument in `wb = openpyxl.load_workbook()`

15) How would you set the height of row 5 to 100?

`sheet.row_dimensions[5].height = 100`

16) How would you hide column C?

I guess you could sett it's width to 0?
`sheet.column_dimensions['C'].width = 0` 

17) What is a freeze pane?

its a frozen row or column that doesn't move when user scrolls the spreadsheet. It's usually used for title fot the data used

18) What five functions and methods do you have to call to create a bar chart?

1) Create a `Reference object` from **rectangular section of cells**
2) Create a `Series object` by passing in `Reference object`
3) Create `Chart object`
4) Append `Series object` to `Chart object`
5) Add the `Chart object` to the `Worksheet object`, optionally specyfying which **cell** should be **top-left** corner of the chart
