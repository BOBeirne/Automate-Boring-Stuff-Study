# Practice Questions
## 1. What is the difference between `shutil.copy()` and `shutil.copytree()`?

`shutil.copy()` copies only one **file**
`shutil.copytree()` copies the whole **folder including subfolders and files inside**
## 2. What function is used to rename files?

`shutil.move()`
## 3. What is the difference between the delete functions in the send2trash and shutil modules?

Delete permanently deletes the file without any way of recovering them
Send to trash move the marked files to the system bin folder
## 4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

`zipfile.ZipFile('zipfile', 'r')` is equivalent to reading zip file

# Practice Programs

## 1. Selectively Copying

Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from their current location to a new folder.

## 2. Deleting Unneeded Files

It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. If you’re trying to free up room on your computer, it’s more effective to identify the largest unneeded files first.

Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB. (Remember that, to get a file’s size, you can use `os.path.getsize()` from the os module.) Print these files with their absolute path to the screen.

## 3. Renumbering Files

Write a program that 
1. finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on... 
2. in a single folder 
3. and locates any gaps in the numbering (such as if there is a spam001.txt and a spam003.txt but no spam002.txt). 
4. Have the program rename all the later files to close this gap.

To create these example files (skipping spam042.txt, spam086.txt, and spam103.txt), run the following code:

```python
for i in range(1, 121):
	if i not in (42, 86, 103):
		with open(f'spam{str(i).zfill(3)}.txt', 'w') as file:
			pass
```

## 4. As an added challenge, write another program that can insert gaps into numbered files (and bump up the numbers in the filenames after the gap) so that a new file can be inserted.

## 5. Converting Dates from American- to European-Style

Say your boss emails you thousands of files with American-style dates (MM-DD-YYYY) in their names and needs them renamed to European-style dates (DD-MM-YYYY). This boring task could take all day to do by hand! Instead, write a program that does the following:

1. Searches all filenames in the current working directory and all subdirectories for American-style dates. Use the `os.walk()` function to go through the subfolders.
2. Uses regular expressions to identify filenames with the MM-DD-YYYY pattern in them—for example, spam12-31-1900.txt. Assume the months and days always use two digits, and that files with non-date matches don’t exist. (You won’t find files named something like 99-99-9999.txt.)
3. When a filename is found, renames the file with the month and day swapped to make it European-style. Use the `shutil.move()` function to do the renaming.