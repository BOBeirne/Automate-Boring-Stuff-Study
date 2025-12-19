# Practice Questions

* What are some features that Excel spreadsheets have but CSV spreadsheets don’t?

They can be opened in excel but lack a couple of excel file functionalities:
- Formatting
- macros
- Formulas / Mathematical equations

* What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

- You need to pass the File Object you create using `open(filename)`


* What modes do File objects for reader and writer objects need to be opened in?

1. you need to use `open()`, 
2. open in `w` write mode or `r` for read mode
3. (optional) you need to include `newline=''` if you are on windows

* What method takes a list argument and writes it to a CSV file?

`csv.writer_object.writerow(list_here)`

* What do the delimiter and lineterminator keyword arguments do?

- Cells use delimiter to separate each cell
- rows use terminator to separate each row

* Of CSV, JSON, and XML, which formats can be easily edited with a text editor application?

All of them, but XML is notoriously hard to uderstand compared to others

* What function takes a string of JSON data and returns a Python data structure?

use `json.loads()` to load string and return a variable, then print that variable out

* What function takes a Python data structure and returns a string of JSON data?

use `json.dumps()` to dump string of python data and convert it to JSON format

* Which data serialization format resembles HTML, with tags enclosed in angle brackets?

XML

* How does JSON write None values?

`null`

* How do you write Boolean values in JSON?

`true` and `false` with lowercase
