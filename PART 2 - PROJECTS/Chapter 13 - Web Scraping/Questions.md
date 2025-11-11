# Module 13 Questions

## 1.  Briefly describe the differences between the `webbrowser`, `requests`, and `bs4` modules.

- `webbrowser` module - built-in python browser that opens a specific page
- `requests` module - downloads files and web pages from web for parsing
- `bs4` module - short for beautifulsoup4. uses parsed HTML or XML downloaded by requests. it creates easily searchable python objects that help you find specific HTML elements

## 2.  What type of object is returned by `requests.get()`? How can you access the downloaded content as a `string` value?

`print(response.text)`

## 3.  What `requests` method **checks** that the download worked?

`print(response.status_code == requests.codes.ok)`

## 4.  How can you get the `HTTP status code` of a `requests` response?

`print(response.raise_for_status())` you can wrap it in except statements as it will stop the program if there is an error
or you can compare `response.status_code` to `requests.codes.ok`

## 5.  How do you **save** a `requests response` to a file?

```python
with open('downloaded.txt', 'wb') as file: # we put the file into variable
	for chunk in response.iter_content(100000): # 100000 is the chunk size
		file.write(chunk) 
```

## 6.  What two formats do most online APIs return their responses in?

- JSon
- XML

## 7.  What is the keyboard shortcut for opening a browser’s Developer Tools?

- F12

## 8.  How can you view (in the Developer Tools) the `HTML` of a specific `element` on a web page?

- Hover over the element and right click -> Inspect. This will open Developer tools and highlight in HTML the element selected

## 9.  What `CSS` selector string would find the element with an id attribute of `main`?

`#main`

## 10.  What `CSS` selector string would find the elements with an id attribute of `highlight`?

`#highlight`

## 11.  Say you have a Beautiful Soup Tag object stored in the variable spam for the element `<div>Hello, world!</div>`. How could you get a string `'Hello, world!'` from the Tag object?

`print(spam.text)`

## 12.  How would you store all the attributes of a **Beautiful Soup** `Tag` object in a variable named `link_elem`?

`link_elem = soup.attrs`

## 13.  Running `import selenium` doesn’t work. How do you properly import Selenium?

`from selenium import webdriver`

## 14.  What’s the difference between the `find_element()` and `find_elements()` methods in Selenium?

- `find_element()` returns the first element that matches the CSS selector.
- `find_elements()` returns a list of all elements that match the CSS selector.

## 15.  What methods do **Selenium’s** `WebElement` objects have for simulating **mouse clicks and keyboard keys**?

```python
link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
link_elem.click() # follows the 'This text is a link' link and clicks on it
link_elem.send_keys('hello') # send 'hello' to the element
```

## 16.  In **Playwright**, what **locator** method call simulates pressing `CTRL-A ` to select all the text on the page?

`page.locator('html').press('Control+A')`

## 17.  How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with **Selenium**?

- `browser.back()` - goes back to the previous page
- `browser.forward()` - goes forward to the next page
- `browser.refresh()` - refreshes the page

## 18.  How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with **Playwright**?

- `page.go_back()`	Navigates back to the previous page in the browser's history.
- `page.go_forward()`	Navigates forward to the next page in the browser's history.
- `page.reload()`	Reloads the current page.