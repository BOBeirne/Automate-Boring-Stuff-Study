# CSV

- **CSV** stands for **Comma-Separated-Values**
- **Data serialization format** used to store data as **plaintext**
- It's a **simplified spreadsheet** format
- works best for **storing variable number of rows of data that share the same columns**
- uses .csv extension

## CSV Format

- Each line in a CSV file represents a **single row of data**
- Each column of data is separated by a comma
- If you were to open an `example3.xlsx` as a **CSV** it would look like this:

```csv
4/5/2035 13:34,Apples,73
4/5/2035 3:41,Cherries,85
4/6/2035 12:46,Pears,14
4/8/2035 8:59,Oranges,52
4/10/2035 2:07,Apples,152
4/10/2035 18:10,Bananas,23
4/10/2035 2:40,Strawberries,98
```

- You can think of it as a list of values
```csv
[['4/5/2035 13:34', 'Apples', '73'], ['4/5/2035 3:41', 'Cherries', '85'], ... ['4/10/2035 2:40', 'Strawberries', '98']]
```

- It is a very simple format, lacks styles and formatting
- It's advantage is very simple format and wide programming support

### csv module

#### Extracting data

- Do **not assume** that between every **comma** there is a is a cell
- CSV file have a **set of escape characters** to allow **commas as part of values**
- Because of that `Split() method` won't work well and **it is recommended to use dedicated module** instead

##### getting a `csv.reader()` object

- `csv` module comes **pre-installed in python**
- You can **import** it with `import csv`
- to **read CSV**, you need to first get `csv.reader() object`
  - **to get it** use `open() function` and pass it to the `csv .reader() function`
  - That should then **return** `csv.reader object`
  - !!! You **cannot pass filename str to csv.reader() directly** !!!

###### using `list()` on csv.reader()

- You can also use a `list()` on the `csv reader object` to view a list of lists
- `list(csv.reader(example_file))`
- once you have a list of lists, you can access values at particular row and column using their index

```python
import csv
example_file = open('example3.csv')
example_reader = csv.reader(example_file) # note you need to pass it variable name not the str filename
example_data = list(example_reader) # easiest way to read data off csv is using a list
print(example_data)
#[['05/04/2035 13:34', 'Apples', '73'], ['05/04/2035 03:41', 'Cherries', '85'], ['06/04/2035 12:46', 'Pears', '14'], ['08/04/2035 08:59', 'Oranges', '52'], ['10/04/2035 02:07', 'Apples', '152'], ['10/04/2035 18:10', 'Bananas', '23'], ['10/04/2035 02:40', 'Strawberries', '98']]

example_data[0][0] # 1st row
# '4/5/2035 13:34'
example_data[0][1] # 1st row, 2nd column
# 'Apples'
example_data[0][2]  # First row, third column
# '73'
example_data[1][1]  # Second row, second column
# 'Cherries'
example_data[6][1]  # Seventh row, second column
# 'Strawberries'

example_file.close() # don't forget to close!
```

##### using `for loop` to access the data

- for **large CSV files**, it may be **easier** to use the `for loop`
- `for` loop will iterate over the list of lists and access the values using their index
- you **can loop through** `reader object` **once**, to re-read csv file again you need to create a **new reader object again**

- To get **row numbers**, use `.line_num attribute`, which stores an **int**
- Unlike Python list indexes, line numbers in `line_num` **begin at 1, not 0.**
	- if csv file uses **headers**, the line number would **start at 2**

```python
import csv
example_file = open('example.csv')
example_reader = csv.reader(example_file)

for row in example_reader:
	print('Row #' +str(example_reader.line_num) + '' + str(row))

# Row #1 ['4/5/2035 13:34', 'Apples', '73']
# Row #2 ['4/5/2035 3:41', 'Cherries', '85']
# Row #3 ['4/6/2035 12:46', 'Pears', '14']
# Row #4 ['4/8/2035 8:59', 'Oranges', '52']
# Row #5 ['4/10/2035 2:07', 'Apples', '152']
# Row #6 ['4/10/2035 18:10', 'Bananas', '23']
# Row #7 ['4/10/2035 2:40', 'Strawberries', '98']
```

#### Writing CSV Files

##### using `csv.writer()`

- First call `open()` to o**pen file in write mode**
  - **Windows specific:** You need to pass a blank string for the `open()` function’s newline keyword argument `newline=''`
- Then **pass** the **file object to** the `csv.writer()` function
- `csv.writer()` function **returns a `writer object`**
- `writerow()` method takes a `list argument`


```python
import csv
output_file = open('output.csv', 'w', newline='') # newline='' is needed to prevent extra line, use w as write mode
csv_writer = csv.writer(output_file)

csv_writer.writerow(['spam', 'eggs', 'bacon', 'ham']) # write row
# 21
csv_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# 32
csv_writer.writerow([1, 2, 3.141592, 4])
# 16
output_file.close()
```

#### Header Rows - DictReader & DictWriter

- `csv.DictReader()` and `csv.DictWriter()` work **like the reader and writer objects**, but they **work with dictionaries** instead of lists
- This helps to read the data from CSV files that have **headers in the 1st row**

#### using `csv.DictReader()`

Example:
We will be using file `exampleWithHeather3.csv` that has **headers in the 1st row**

```python
import csv

example_file = open('exampleWithHeader3.csv') # open the file
example_dict_reader = csv.DictReader(example_file) # create a DictReader object
example_dict_data = list(example_dict_reader) # read the data into a list of dictionaries

print(example_dict_data) # print the list of dictionaries
# [{'Timestamp': '4/5/2025 13:34', 'Fruit': 'Apples', 'Quantity': '73'}, {'Timestamp': '4/5/2025 3:41', 'Fruit': 'Cherries', 'Quantity': '85'}, {'Timestamp': '4/6/2025 12:46', 'Fruit': 'Pears', 'Quantity': '14'}, {'Timestamp': '4/8/2025 8:59', 'Fruit': 'Oranges', 'Quantity': '52'}, {'Timestamp': '4/10/2025 2:07', 'Fruit': 'Apples', 'Quantity': '152'}, {'Timestamp': '4/10/2025 18:10', 'Fruit': 'Bananas', 'Quantity': '23'}, {'Timestamp': '4/10/2025 2:40', 'Fruit': 'Strawberries', 'Quantity': '98'}]

# you need to open the file again if you want to make another operation
example_file = open('exampleWithHeader3.csv') # open the file
example_dict_reader = csv.DictReader(example_file) # create a DictReader object

# Use the for loop to print the data
for row in example_dict_reader:
	print(row['Timestamp'], row['Fruit'], row['Quantity'])
# 4/5/2025 13:34 Apples 73
# 4/5/2025 3:41 Cherries 85
# 4/6/2025 12:46 Pears 14
# 4/8/2025 8:59 Oranges 52
# 4/10/2025 2:07 Apples 152
# 4/10/2025 18:10 Bananas 23
# 4/10/2025 2:40 Strawberries 98
```

##### csv.DictReader with Header-less file

- If file does not have headers in the first row, it will use the 1st row as headers
- To avoid it, you can pass `csv.DictReader()` a second argument with names for the headers

```python
import csv

example_file = open('example3.csv') # open the file without headers
example_dict_reader = csv.DictReader(example_file, ['Timestamp', 'Fruit', 'Quantity']) # create a DictReader object and pass it the header names

for row in example_dict_reader:
	print(row['Timestamp'], row['Fruit'], row['Quantity'])
# 4/5/2025 13:34 Apples 73
# 4/5/2025 3:41 Cherries 85
# 4/6/2025 12:46 Pears 14
# 4/8/2025 8:59 Oranges 52
# 4/10/2025 2:07 Apples 152
# 4/10/2025 18:10 Bananas 23
# 4/10/2025 2:40 Strawberries 98
```

##### csv.DictWriter

- to create a CSV file with headers, use `csv.DictWriter()`
- `csv.DictWriter()` works **like the writer object**, but it **works with dictionaries** instead of lists
- To insert header, use `.writeheader()` on the writer object, if you don't want the header row you can skip it completely.

Example:

```python
import csv
output_file = open('output.csv', 'w', newline='') # open the file in write mode, for windows include the newline argument!
output_dict_writer = csv.DictWritter(output_file, ['Name','Pet','Phone']) # create a DictWriter object and pass it the header names
output_dict_writer.writeheader() # add a row of headers, skip it if you don't want headers

# write rows
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'Cat', 'Phone': '555-5555'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'}) # this will leave empty 'Pet' column
output_dict_writer.writerow({'Phone': '555-1234', 'Name': 'Carol', 'Pet': 'dog'}) # order of key entry does not matter as long as keys are the same

output_file.close() # save the file
```

Output file:
```csv
Name,Pet,Phone
Alice,cat,555-1234
Bob,,555-9999
Carol,dog,555-5555
```

- double commas `,,` indicate a missing key (Bob's pet)