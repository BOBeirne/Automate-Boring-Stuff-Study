# requests module

[Docs](https://requests.readthedocs.io/en/latest/)

- `requests` module needs to be installed
- `requests.get()` function takes a str representing URL to download
	- returns `response object`

```python
import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(response))
# <class 'requests.models.Response'>
print(response.status_code == requests.codes.ok) # this is how you check if a request was successful
# True
print(len(response.text))
# 174126
print(response.text[:200])
# The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

#This eBook is for the use of anyone anywhere at no cost and with
#almost no restrictions whatsoever.  You may copy it, give it a
```

### Checking for errors

- You can compare the `response.status_code` to `requests.codes.ok`
- **Easier** way is to use `call_for_status()` method on the `response` object to check for errors
	- it will halt the program if there is an error
	- you can wrap it with the `except` statement
	- It is **good practice** to always call raise_for_status() after calling requests.get()

```python
import requests
response = requests.get('https://inventwithpython.com/page_that_does_not_exist')
print(response.raise_for_status())
```

### Saving Downloaded Files to the Hard Drive

- once the page is downloaded, you can save it to the hard drive using open() and write() methods 
	- they **must be opened in binary mode** by passing `wb` as a  second attribute to open() to maintain the Unicode encoding
- to write the web page to a file you can use a `for` loop with the `Response` object's `iter_content()` method

```python
import requests
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status() # check for any issues downloading

with open('RomeoAndJuliet.txt', 'wb') as file: # we put the file into variable
	for chunk in response.iter_content(100000): # 100000 is the chunk size
		file.write(chunk) 

print('File RomeoAndJuliet.txt has been saved to the hard drive.')
```
- `iter_content()` method returns “chunks” of the content on each iteration through the loop. 
	- Each chunk is of the `bytes` data type, and you get to specify how many bytes each chunk will contain. 
	- One hundred thousand bytes (100000) is generally a good size, so pass 100000 as the argument to `iter_content()`.



