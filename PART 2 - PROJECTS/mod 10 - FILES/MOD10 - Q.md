## Practice Questions

### 1. What is a relative path relative to?

Relative to current location of current working directory
### 2.  What does an absolute path start with?

Root directory
### 3.  What does Path('C:/Users') / 'Al' evaluate to on Windows?

C:\Users\Al
### 4.  What does 'C:/Users' / 'Al' evaluate to on Windows?

It results in TypeError as you need to specify Path method in Pathlib to use

### 5.  What do the os.getcwd() and os.chdir() functions do?

* os.getcwd() gets the current working directory path
* os.chdir() is a way to change a current working directiory

### 6. What are the . and .. folders?

when using relative path
* . is specifying current folder
* .. is specifying parent folder

### 7.  In C:\bacon\eggs\spam.txt, which part is the directory name, and which part is the base name?

* Directory - C:\bacon\eggs
* Base name - spam.txt

### 8. What three “mode” arguments can you pass to the open() function for plaintext files?

* `'w'` to write files
* `'r'` to read files
* `'a'` to append files

### 9. What happens if an existing file is opened in write mode? 

It writes new data into the opened file while overwriting the contents
### 10.  What is the difference between the read() and readlines() methods? 

* read() method reads the content of file as one long string
* readlines() uses \n characters to split the long string into separate values and it then returns a list of string values, where each string is one line of the file.
### 11.  What data structure does a shelf value resemble?

Dictionary


## Practice Programs
For practice, design and write the following programs.

### Mad Libs
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace them:

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
It would then create the following text file:

The silly panda walked to the chandelier and then screamed. A nearby
pickup truck was unaffected by these events.
The program should print the results to the screen in addition to saving them to a new text file.

### Regex Search
Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression, then prints the results to the screen.