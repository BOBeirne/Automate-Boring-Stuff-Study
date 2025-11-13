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
			- each `cell` can contain one or more `values`