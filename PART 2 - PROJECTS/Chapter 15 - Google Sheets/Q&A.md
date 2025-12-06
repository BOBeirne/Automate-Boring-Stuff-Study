# Practice Questions
 
1)  What three files do you need for EZSheets to access Google Sheets?

- credentials-sheets.json
- token-drive.pickle
- token-sheets.pickle

2)  What two types of objects does EZSheets have?

- Sheet object
- Spreadsheet object

3)  How can you create an Excel file from a Google Sheets spreadsheet?

- Yes, you can download sheets file from google as .xlsx file using `ss.downloadAsExcel()`

4)  How can you create a Google Sheets spreadsheet from an Excel file?

- yes you can upload excel spreadsheet into sheets and it will convert it while uploading

5)  The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled Students?

```python
sheet = ss['Students'] # put the sheet object into variable 
cell_val = sheet['B2'].value # access the cell value of the variable
```

6)  How can you find the column letters for column 999?

`ezsheets.getColumnLetterOf(999)`

7)  How can you find out how many rows and columns a sheet has?

```python
# after importing ezsheets, putting sheet into ss variable and then sheet into sheet variable:
print(sheet.rowCount) #  show how many rows are in the spreadsheet
print(sheet.columnCount) # shows how many columns there are in a spreadsheet
```

8)  How do you delete a spreadsheet? Is this deletion permanent?

- you can move spreadsheet to bin folder using `ss.delete()`
- You can permanently delete the spreadsheet if you use pass True as an optional argument `ss.delete(permanent=True)`

9)  What functions will create a new Spreadsheet object and a new Sheet object, respectively?

```python
ss = ezsheets.Spreadsheet() # brand new spreadsheet in variable ss, it creates a default "Sheet1" sheet
ss.sheet('New Sheet') # creates new sheet called "new sheet"
sheet = ss.sheets[0] # to select the first, default spreadsheet and put it in variable
```

10)  What would happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?

You will receive an exception called ``googleapiclient.errors.HttpError “Quota exceeded for quota group”``