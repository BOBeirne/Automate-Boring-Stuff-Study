# EZSheets 

- Docs: https://github.com/AlSweigart/EZSheets
- needs to be installed `python -m pip install EZSheets`
- **Requires a setup** to obtain **Credentials .json and tokens** files from [Google Cloud Console](https://console.cloud.google.com/) to grant the API access to your account for Sheets and Drive

## Setting Up EZSheets

- Before your Python scripts can use EZSheets to access and edit your Google Sheets spreadsheets, you need a **credentials JSON file and two token JSON files.**
- Setup is as follows:
	1) Create a **new Google Cloud project**.
	2) Enable the Google **Sheets API and Google Drive API** for your project.
	3) Configure the **OAuth consent** screen.
	4) Create **credentials file**.
	5) **Log in** with the credentials file to generate **token files**.
- This setup needs to be done **only once per project.**

#### This setup UI has been slightly changed since the book was written, this is the updated way as of November 2025

### 1) Create New Google Cloud Project

 1) got to [Google Cloud Console](https://console.cloud.google.com/)
 2) Create a new project and give it a name (e.g. EZSheets)
	- Free Google accounts can have up to 12 projects but you only need 1 project for this setup

### 2) Enable APIs

1) Select the project you just created from the list of projects
2) Open the side menu -> Click on the **APIs & Services** -> Library
3) search for **Sheets API** or **Drive API**
4) Enable the API (click on the **Enable** button)
5) repeat for the other one

### 3) Enable OAuth Consent Screen

1) Open the **side menu** -> Click on the **APIs & Services** -> **OAuth** consent screen
2) Run the setup -> Click on the **Create** button and make it **External**
3) Click on the **Create** button

### 4) Select Scopes for each API

1) In the OAuth side menu, select the Data access page
2) Select "Add or remove scopes"
3) Select the **Sheets** `.../auth/spreadsheets` and **Drive** `.../auth/drive`scopes for your project
4) Click on the **Save** button and then again **Save**

### 5) Add Test User(s)

1) Open the side menu -> Click on the **APIs & Services** -> Audience
2) Click on the **+ Add users** button
3) Type in the google email address of a test user
4) Click on the **Save** button

### 6) Create Credentials .json file

1) Open the side menu -> Click on the **APIs & Services** -> Clients
2) Select **+Create Client**
3) Create access for Desktop application and name it whatever you want
4) Click on the **Save** button
5) Download the **credentials.json** file to a safe location
6) rename the file to `credentials-sheets.json`

### 7) Generate token files

- Open the python CLI in the same folder as your credentials JSON file
- Navigate to location of the .json file and run `import ezsheets`. 
	- EZSheets automatically checks the current working directory for the credentials JSON file by calling the `ezsheets.init() function`. 
- If the file is found, EZSheets launches your **web browser** to the **OAuth consent** screen to generate token files. 
- EZSheets also requires token files, named `token-drive.pickle` and `token-sheets .pickle`, along with the `credentials file` to access spreadsheets. 
	- Generating **token** files is a **one-time setup** step that won’t happen the next time you run `import ezsheets`.
	- Sign in with your test user account
	- You will receive a message "“Google hasn’t verified this app”" which you can ignore as it is not an actual app and you are the creator.
	- needs to be repeated for each API (in this case the Sheets and Drive APIs)
	- After closing the second window, you should now see token-drive.pickle and token-sheets.pickle files in the same folder as your credentials JSON file.

#### Revoking the Credentials File

- If ever needed to delete the credentials you need to remove the link to them in console.
- In the [Google Console](https://console.developers.google.com/) go to credentials and click the **bin icon** to delete the credentials associated with the project. 
- This will revoke any connection between the **.json and token files** and the project. There is no need to delete the token files.

---

## google Sheets

- [Google Sheets API](https://developers.google.com/workspace/sheets/api/guides/concepts)

### Spreadsheet object

- Exactly same concept as **Excel spreadsheets** from Chapter 14
	- A `spreadsheet` is a collection of one or more **worksheets**.
	- A `worksheet` is a collection of **one or more rows** and one or more **columns**.
	- A `row` or a `column` is a collection of one or more cells.
	- A `cell` is a container for a single value.
- an example of a `spreadsheet` object can be viewed in the browser [https://autbor.com/examplegs]

#### Creating, Uploading and Listing Spreadsheets


- You can make a **new Spreadsheet object** from an existing Google Sheets spreadsheet, a new blank spreadsheet, or an uploaded Excel spreadsheet.
- All Google Sheets spreadsheets have a unique ID that can be found in their URL, after the spreadsheets/d/ part and before the /edit part.
	- in example `https://docs.google.com/spreadsheets/d/1TzOJxhNKr15tzdZxTqtQ3EmDP6em_elnbtmZIcyu8vI/edit#gid=0/`
	- The ID is `1TzOJxhNKr15tzdZxTqtQ3EmDP6em_elnbtmZIcyu8vI`
- Google Sheets spreadsheet is represented as an `ezsheets.Spreadsheet object`, which has **id, url, and title** attributes. 

```python
import ezsheets
ss = ezsheets.Spreadsheet()

ss.title
# 'Title of My New Spreadsheet'
ss.url
# 'https://docs.google.com/spreadsheets/d/1gxz-Qr2-RNtqi_d7wWlsDlbtPLRQigcEXvCtdVwmH40/'
ss.id
# '1gxz-Qr2-RNtqi_d7wWlsDlbtPLRQigcEXvCtdVwmH40'
```

#### Loading an Existing Spreadsheet

- Pass `ezsheets.Spreadsheet()` either:
	- ID
	- IRL
	- URL that redirects to the spreadsheet

```python
import ezsheets
ss1 = ezsheets.Spreadsheet('https://autbor.com/examplegs')
ss2 = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1TzOJxhNKr15tzdZxTqtQ3EmDP6em_elnbtmZIcyu8vI/')
ss3 = ezsheets.Spreadsheet('1TzOJxhNKr15tzdZxTqtQ3EmDP6em_elnbtmZIcyu8vI')

ss1 == ss2 == ss3
# True (they are the same spreadsheet object)
```

#### Upload existing spreadsheet

- Pass the filename to `ezsheets.upload()` function
- You can upload Excel, OpenOffice, CSV, or TSV spreadsheet to Google Sheets

```python
import ezsheets
ss = ezsheets.upload('examplegs.xlsx')
ss.title
# 'examplegs'
```

#### List Spreadsheets

- list the spreadsheets in your **Google account** by calling the `listSpreadsheets()`
- Returns a **dictionary** whose **keys are spreadsheet IDs** and whose **values are the titles** of each spreadsheet
	- It **includes deleted spreadsheets** in your account’s Trash folder

```python
import ezsheets
ezsheets.listSpreadsheets()
# {} # empty dictionary
```

### Spreadsheet Attributes

- Data lives in actual sheets within spreadsheet objects, we can manipulate spreadsheet itself using following attributes:
	- `title`
	- `url`
	- `id`
	- `sheets`
	- `sheetTitles`

```python
import ezsheets
example_ss = ezsheets.Spreadsheet('https://autbor.com/examplegs') # load spreadsheet from URL
ss = ezsheets.Spreadsheet() # create new spreadsheet
example_ss.sheets[0].copyTo(ss) # copy first sheet from example spreadsheet to new spreadsheet
ss.sheets[0].delete() # delete first sheet from new spreadsheet

ss.url # retrieve url for the new spreadsheet
# 'https://docs.google.com/spreadsheets/d/1HWAuHENWqVToRWyPA1r0QL7mGJY2UCJKV4I5ei2jEDk/'
ss.id 
# '1HWAuHENWqVToRWyPA1r0QL7mGJY2UCJKV4I5ei2jEDk'
ss.title
# 'Untitled spreadsheet'
ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet
# ('Copy of Books',)
ss.sheets
# (<Sheet sheetId=401305097, title='Copy of Books', rowCount=1000, columnCount=26>,)
ss.sheets[0]  # The first Sheet object in this Spreadsheet
# <Sheet sheetId=401305097, title='Copy of Books', rowCount=1000, columnCount=26>
ss['Copy of Books']  # Sheets can also be accessed by title.
# <Sheet sheetId=401305097, title='Copy of Books', rowCount=1000, columnCount=26>
ss.Sheet('New blank sheet')  # Create a new sheet.
ss.sheets
# (<Sheet sheetId=401305097, title='Copy of Books', rowCount=1000, columnCount=26>, <Sheet sheetId=906018579, title='New blank sheet', rowCount=1000, columnCount=26>)
ss.sheets[1].delete()  # Delete the second Sheet object in this Spreadsheet.
ss.sheets
# (<Sheet sheetId=401305097, title='Copy of Books', rowCount=1000, columnCount=26>,)
```

### Refreshing Data

- use `refresh()` method to **refresh** the data in the spreadsheet to match the online version
- This will **refresh Spreadsheet object’s attributes and also the data** in the Sheet objects it contains. 
- You’ll see the changes you make to the Spreadsheet object applied to the **online spreadsheet in real time.**

### Downloading and Uploading Spreadsheets

- You can **download** the spreadsheet as a **ODS, CSV, XLSX, PDF or TSV** file by calling the `download()` method on the spreadsheet object.
- You can also download a `.zip` file containing `HTML` files of spreadsheet data

```python
import ezsheets
ss = ezsheets.Spreadsheet('https://autbor.com/examplegs')
ss.title
# 'Sweigart Books (DO NOT DELETE)'
ss.downloadAsExcel() # download spreadsheet as Excel file
# 'Sweigart_Books.xlsx'
ss.downloadAsODS() # download spreadsheet as OpenOffice file
# 'Sweigart_Books.ods'
ss.downloadAsCSV() # download spreadsheet as CSV file
# 'Sweigart_Books.csv'
ss.downloadAsPDF() # download spreadsheet as PDF file
# 'Sweigart_Books.pdf'
ss.downloadAsTSV() # download spreadsheet as TSV file
# 'Sweigart_Books.tsv'
ss.downloadAsHTML() # download spreadsheet as ZIP file with HTML files
# 'Sweigart_Books.zip'

ss.downloadAsExcel('a_different_filename.xlsx') # you can also change the filename of the downloaded file before downloading
#'a_different_filename.xlsx'
```

####  files in the CSV or TSV format can contain only one sheet

- if you download in `CSV` or `TSV` format you will only get the first sheet in the spreadsheet
- to download other sheets, you need to re-order sheets before downloading for the sheet to be first in the file

### Deleting Spreadsheets

- You can **delete** a spreadsheet by calling the `delete()` method on the spreadsheet object.
- It will move the spreadsheet to the Trash folder, it will still appear in the `listSpreadsheets()` function
	- to permanently delete it, pass `permanent=True` to the `delete()` function
	- Generally bad idea because it's not reversible and if bug deletes the wrong spreadsheet it will be unrecoverable

```python
import ezsheets
ss.delete(permanent=True)
# {}
```
### Sheet Object

- `Spreadsheet object` will have **1+** `Sheet objects`
- each `Sheet object` represents **rows and columns of data** in the spreadsheet
- You can **access those sheets** using `[]` and `integer index`
- Once you have a `Sheet object`, you can **read data from it and write data to it** using the `Sheet object’s methods`

- `Spreadsheets object's **Sheet** attributes` contain a **tuple** of `sheet objects` in the order of which they appear in the spreadsheet
- `Spreadsheet object’s sheetTitles attribute` holds a **tuple **of all the `sheet titles`.

```python
import ezsheets

ss = ezsheets.Spreadsheet()
sheet2 = ss.Sheet('Spam') # create a new sheet called 'Spam'
sheet3 = ss.Sheet('Eggs') # create a new sheet called 'Eggs'

ss.sheets
# (<Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>, <Sheet sheetId=1716414623, title='Spam', rowCount=1000, columnCount=26>, <Sheet sheetId=566299236, title='Eggs', rowCount=1000, columnCount=26>)

ss.sheets[0]  # Gets the first Sheet object in this Spreadsheet
# <Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>

ss.sheetTitles  # The titles of all the Sheet objects in this Spreadsheet
# ('Sheet1', 'Spam', 'Eggs')
```

### Reading and Writing Data 

- **Just as in Excel**, Google Sheets worksheets have **columns and rows of cells containing data.**
- You can **use** the square brackets operator `[]` to **read and write data from and to these cells**
- writing values to the online spreadsheet requires a network connection and can take about a second

```python
import ezsheets
ss = ezsheets.Spreadsheet()

ss.title = 'My Spreadsheet' # set the title of the spreadsheet to 'My Spreadsheet'
sheet = sssheets[0] # get the first sheet in the spreadsheet
sheet.title
# 'Sheet1'
sheet['A1'] = 'Name' # set the value of cell A1 to 'Name'
sheet['B1'] = 'Age' # set the value of cell B1 to 'Age'
sheet['C1'] = 'Favorite Movie' # set the value of cell C1 to 'Favorite Movie'

sheet['A1'] # get the value of cell A1
# 'Name'
sheet['A2'] # get the value of cell A2, empty cells return blank strings
# ''

sheet[2,1] # get the value of cell B2 (col 2, row 1)
# 'Age'

sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['C2'] = 'RoboCop'

sheet['B2']  # all data is returned as strings.
'30'
```


### Addressing Columns and Rows

- Cell addressing works in Google Sheets **just like in Excel. **
- You can **convert** from the **'A2' string-style address** to the **(column, row) tuple-style address** (and vice versa) with the `convertAddress() function`.
- The `getColumnLetterOf()` and `getColumnNumberOf() functions` will **also convert a column address between letters and numbers**
- The `(column, row) tuple-style addresses` are convenient if you’re **looping over a range of addresses and need a numeric identifier for the column**. 
- The other functions are helpful when you need to convert between the two formats.

```python
import ezsheets
ezsheets.convertAddress('A2')  # Converts addresses...
# (1, 2)
ezsheets.convertAddress(1, 2)  # ...and converts them back, too.
# 'A2'
ezsheets.getColumnLetterOf(2)
# 'B'
ezsheets.getColumnNumberOf('B')
# 2
ezsheets.getColumnLetterOf(999)
# 'ALK'
ezsheets.getColumnNumberOf('ALK')
# 999
ezsheets.getColumnNumberOf('ZZZ')
# 18278
```

### Reading and Writing Entire Columns and Rows

- You can **read and write entire columns and rows** of cells at once using `getColumn()`, `getRow()`, `updateColumn()`, and `updateRow()` methods
- These methods make **requests** to the Google Sheets servers to update the spreadsheet, so you **must have a network connection.**

Example:
- we will **upload** `produceSales3.xlsx` from **Chapter 14** to Google Sheets
	- place file in current folder. 

```python
import ezsheets
ss = ezsheets.upload('produceSales3.xlsx') # upload produceSales3.xlsx to Google Sheets
sheet = ss.sheets[0] # get the first sheet in the spreadsheet

sheet.getRow(1) # get the first row in the spreadsheet
# ['PRODUCE', 'COST PER POUND', 'POUNDS SOLD', 'TOTAL', '', '']
sheet.getRow(2) # get the second row in the spreadsheet
# ['Potatoes', '0.86', '21.6', '18.58', '', '']

sheet.getColumn(1) # get the first column in the spreadsheet
# ['PRODUCE', 'Potatoes', 'Okra', 'Fava beans', 'Watermelon', 'Garlic',(...)]
sheet.getColumn('A') # get the first column in the spreadsheet (same as above)
# ['PRODUCE', 'Potatoes', 'Okra', 'Fava beans', 'Watermelon', 'Garlic',(...)]

sheet.getRow(3) # get the third row in the spreadsheet
# ['Okra', '2.26', '38.6', '87.24', '', '']

sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230']) #  change the values in the third row
sheet.getRow(3) # get the third row in the spreadsheet
# ['Pumpkin', '11.50', '20', '230', '', ''] # Note that the rows in the Google Sheets spreadsheet have empty strings at the end.

columnOne = sheet.getColumn(1) # get the first column in the spreadsheet

for i, value in enumerate(columnOne): # loop through the values in the first column 
	columnOne[i] = value.upper() # change all the values in the first column to uppercase

sheet.updateColumn(1, columnOne) # update the first column in the spreadsheet in one request

ss.url
# 'https://docs.google.com/spreadsheets/d/1uJJrUralRlGM92hIAV3eNK4FQ2-DwkvU4O46zyprKl0/'
```

### Changing size of a spreadsheet

- Note that the **rows** in the spreadsheet have **empty strings at the end**.
- This is because the **uploaded sheet has a column count of 6, but we have only four columns of data**. 
- You can **read the number of rows and columns** in a sheet with the `rowCount` and `columnCount attributes`.
- You can change the size of the spreadsheet by setting values to those attributes.
- Google Sheets spreadsheets can have up to 10 million cells

```python
import ezsheets
ss = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1uJJrUralRlGM92hIAV3eNK4FQ2-DwkvU4O46zyprKl0/') # lets work on last uploaded spreadsheet

sheet.rowCount # get the number of rows in the spreadsheet
# 23758
sheet.columnCount # get the number of columns in the spreadsheet
# 6
sheet.columnCount = 4 # change the number of columns in the spreadsheet to 4
sheet.columnCount # get the number of columns in the spreadsheet
# 4
```

### Creating, Moving, and Deleting Sheets

- **All new** spreadsheets come with one, default sheet called `Sheet1`.
- You can a**dd new sheet** with `Sheet()` method which takes an **optional** `title` parameter and **index** parameter to specify position.
- You can also move the index of the sheet using the `.index` parameter.
- To **delete a sheet**, use the `.delete()` method on the sheet object. You can **select** them by **name or index**.

```python
import ezsheets
ss = ezsheets.Spreadsheet() # create new spreadsheet

ss.title('MultipleSheets') # set the title of the spreadsheet to 'MultipleSheets'

ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet
# ('Sheet1',)

ss.Sheet('Spam') # create a new sheet called 'Spam'
ss.Sheet('Eggs')  # Create another new sheet.

ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet
# ('Sheet1', 'Spam', 'Eggs')

ss.Sheet('Bacon', 0) # Create a new sheet called 'Bacon' before the first sheet.
ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet
# ('Bacon', 'Sheet1', 'Spam', 'Eggs')

ss.sheets[0].index = 2 # move the first sheet to the second position
ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet
# ('Sheet1', 'Spam', 'Bacon', 'Eggs')
ss.sheets[2].index = 0 # move the third sheet to the first position
ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet
# ('Bacon', 'Sheet1', 'Spam', 'Eggs')

ss.sheets[0].delete() # Delete the first Sheet object in this Spreadsheet.
ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet
# ('Sheet1', 'Spam', 'Eggs')
ss['Spam'].delete()  # Delete the "Spam" sheet.
ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet
# ('Sheet1', 'Eggs')
sheet - ss['Eggs'] # Get the "Eggs" sheet and put it in a variable called "sheet".
sheet.delete() # Delete the "Eggs" sheet.
ss.sheetTitles # The titles of all the Sheet objects in this Spreadsheet
# ('Sheet1',)
```

#### Deleting sheets is permanent! there’s no way to recover the data

### Copying Sheets

- You can **copy a sheet** using the `.copyTo()` method on the sheet object.