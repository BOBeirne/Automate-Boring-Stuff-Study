## Modules used in this chapter

- webbrowser - built-in python browser that opens to specific page - see project file
- requests - downloads files and web pages from internet
- BeautifulSoup (bs4) - parses downloaded html file to extract the info you're looking for
- Selenium - launches and controls the webbrowser (filling in forms, simulating mouse clicks)
- json - used to parse json files

# Downloading Web Pages

## requests module

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

## [[API]]

- API - Application Programming Interface
	- specification that defines how one piece of software (eg. Python program) can communicate with another piece of software (eg. web server with weather information)
	- even if API is free almost all online service will require registration. You can use temp e-mail service like [10minuteemail.com](https://10minutemail.com/)
	- Many HTTP APIs deliver their responses as one large string. This string is often formatted as JSON or XML. 
	- `json.loads(response.text)` returns a Python data structure of lists and dictionaries containing the JSON data in response.text.


### Breaking down the API URL formatting

- We will be using [OpenWeatherMap](https://openweathermap.org/) API to get weather information
	- [API docs](https://openweathermap.org/api)
	- The free account tier limits you to making 60 API requests per minute.
	- Keep this API key a **secret**! Anyone with this key can make API requests credited to your account.
		- If you write a program that uses an API key, consider having the program read a text file that contains the key instead of including the API key directly in your source code. This way, you can share your program with others (who can sign up for their own API key) without worrying about exceeding the API request limits of your account.

- The URL is:
	- `https://` The scheme used to access the server, which is the protocol name (almost always HTTPS for online APIs) followed by a colon and two forward slashes.
	- `api.openweathermap.org` The domain name of the web server that handles the API request.
	- `/geo/1.0/direct` The path of the API.
		- To avoid confusion when updating an API, most online services include a version number as part of the URL. Over time, a service may release new versions of the API and deprecate older versions. At this point, you’ll have to update the code in your scripts to continue to make use of them
	- `?q={city_name},{state_code},{country_code}&appid={API_key}` The URL’s query string
		- The state code refers to the state’s abbreviation and is required only for cities in the United States
		- The country code is the two- or three-letter [ISO 3166 code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)For example, use the code 'US' for the United States or 'NZ' for New Zealand.

	- You can take the endpoint URL (with the completed query string) and paste it into your web browser to view the response text directly. 
	- This is often a good practice when you’re first learning how to use an API. 
	- The response text for web-based APIs is most often formatted in JSON or XML.

- There are all kinds of other free weather APIs for example: 
	- https://weather.gov
	- https://www.weatherapi.com/

- there may be also weather packages available for Python for example:
	- https://pypi.org/project/pyowm/
	- https://pypi.org/project/openweathermapy/


### Using the API

```python
import requests
city_name = 'San Francisco'
state_code = 'CA'
country_code = 'US'
API_key = '___' # Put your API here
response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}') # URL is called an  [[Endpoint]]

print(response.text) # returns Python string

import json
response_data = json.loads(response.text)
print(response_data) # Returns Python data structure
```

- The returned data is a list whose first element is a dictionary that contains the latitude and longitude of the city.

```python
response_data[0]['lat']
response_data[0]['lon']
```

- URL used to make the API request is called **[[Endpoint]]**
- f-strings in this example replace the city name, state code, and country code into the URL.
- if we didn't use f-strings, we would have to replace the city name, state code, and country code into the URL manually like this:
	`direct?q=San Francisco,CA,US&appid=30ee784a80d81480dab1749d33980112'`

### Finding temperature of San Francisco

- We can use the latitude and longitude of San Francisco to make another API request to OpenWeatherMap to get the temperature of San Francisco
- The temperature returned will be in Kelvin

```python
import requests, json

lat = json.loads(response.text)[0]['lat']
lon = json.loads(response.text)[0]['lon']
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
response_data = json.loads(response.text)
print(response_data) # {'coord': {'lon': -122.4199, 'lat': 37.779}, 'weather': [{'id': 803, --snip-- 'timezone': -25200, 'id': 5391959, 'name': 'San Francisco', 'cod': 200}
print(response_data['main']['temp']) # 285.44 in Kelvins

rounded_temp_C = round(response_data['main']['temp'] - 273.15) # convert Kelvin to Celcius
print(f'Temperature in San Francisco is {rounded_temp_C} C') # 28

rounded_temp_F = round(response_data['main']['temp'] * (9/5) - 459.67) # convert Kelvin to Fahrenheit
print(f'Temperature in San Francisco is {rounded_temp_F} F') # 54.1
```

### Requesting a Latitude and Longitude

- Endpoint: `https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}`
- If OpenWeather is unable to locate the city, response_data will be an empty list.
- If the city name matches multiple responses, the list in response_data will contain different dictionaries at response_data[0], response_data[1], and so on.

```python
import requests, json
response_data[0]['lat'] # returns latitude as a float
response_data[0]['lon'] # returns longitude as a float
```	

### Fetching the Current Weather

- Endpoint: `https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}`
- After converting the response JSON text into a Python data structure in a variable named response_data, you can retrieve the following information:

```python
response_data['weather'][0]['main'] # Holds a string description, such as 'Clear', 'Rain', or 'Snow'
response_data['weather'][0]['description'] # Holds a more detailed string, such as 'light rain', 'moderate rain', or 'extreme rain'
response_data['main']['temp'] # Holds the current temperature in Kelvin
response_data['main']['feels_like'] # Holds the feels-like temperature in Kelvin
response_data['main']['humidity'] # Holds the humidity as a percentage
response_data['wind']['speed'] # Holds the wind speed in meters per second
```

If you supplied an incorrect latitude or longitude argument, response _data will be a dictionary, like {"cod":"400","message":"wrong latitude"}.

### Getting a Weather Forecast

Endpoint for 5-day forecast is `https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}`

```python
response_data['list'] # Holds a list of dictionaries containing the weather predictions for a given time.
response_data['list'][0]['dt'] # Holds a timestamp in the form of a Unix epoch float. Pass this value as an argument to datetime.datetime.fromtimestamp() to obtain the timestamp as a datetime object.
response_data['list'][0]['main'] # Holds a dictionary with keys like 'temp', 'feels_like', 'humidity', and others.
response_data['list'][0]['weather'][0] # Holds a dictionary of descriptions with keys like 'main', 'description', and others.
```

## HTML

- Use of webscraping requires at least basic knowledge of HTML and CSS
- you can learn more about HTML here
	- [Mozilla HTML docs](https://developer.mozilla.org/en-US/docs/Learn/HTML)
	- [FreeCodeCamp](https://www.freecodecamp.org/news/html-coding-introduction-course-for-beginners)
	- [Khan Academy](https://www.khanacademy.org/computing/computer-programming/html-css)

- Some HTML elements have an `id` attribute used to uniquely identify the element in the page. You’ll often instruct your programs to seek out an element by its id attribute, so finding this attribute using the browser’s Developer Tools is a common task when writing web scraping programs.

### Viewing a Web Page’s Source Code

- To see page's HTML code right-click any web page in your web browser (or CTRL-click it on macOS), and select View Source or View page source
- It’s fine if you don’t fully understand what you’re seeing. You just need enough knowledge to pick out data from an existing site.

### Web Browser Developer Tools

- Press F12 to make the toolbar appear
- Pressing F12 again will make it disappear.
- Right-click any part of the web page and select Inspect Element from the context menu to bring up the HTML responsible for that part of the page. This will help you parse HTML for your web scraping programs.

#### **DO NOT** USE REGEX WITH HTML PARSING

Locating a specific piece of HTML (or a piece of XML, JSON, TOML, or YAML) in a string seems like a perfect case for regular expressions. The advice is not to do this. 
HTML can be formatted in many ways and still be considered valid, but trying to capture all these possible variations in a regular expression is tedious and error prone. 

Using a module developed specifically for parsing HTML, such as bs4, is less likely to result in bugs.
You can find an extended argument for why you shouldn’t parse HTML with regular expressions at https://stackoverflow.com/a/1732454/1893164.

### Finding HTML Elements

- Once you have web page HTML as a string value using `requests` module you can start looking for specific HTML elements that interest you.
- This is where Developer Tools can help.
	- When you fo to the website, do little reasearch to find the element you want to scrape.
	- Right-click the element and select Inspect Element
	- The HTML code for the element will appear in the bottom of the page.
	- **Note:** if website changes design of it's elements, the HTML code will be different, so your code will need to be changed too.

For example:

- Go to https://weather.gov/
- Enter the name of the city of your choice or a ZIP code
- Right-click the today's forecast element you want to scrape and select Inspect Element
- Notice the HTML code responsible for the forecasts
```HTML
<div class="col-sm-10 forecast-text">Partly sunny, with a high near 64. Southwest wind 7 to 16 mph, with gusts as high as 31 mph. </div>
```
- It seems that the forecast information is contained inside a <div> element with the forecast-text CSS class.
- Right-click this element in the browser’s developer console -> select Copy (CSS) Selector -> Copies a string such as `'div.row-odd:nth-child(1) > div:nth-child(2)'` to the clipboard. 
	- You can pass it to Beautiful Soup’s select() method 
	- or Selenium’s find_element() method
- CSS selector syntax used in this string specifies which HTML elements to retrieve from a web page

#### when a website changes its layout, you’ll need to update the HTML tags your scripts check. Be sure to keep an eye on your program in case it suddenly displays errors about not being able to find elements.

## Parsing HTML with BeautifulSoup

- Documentation can be found [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Requires to be installed with `pip install beautifulsoup4` , `bs4` to import
- BeautifulSoup is a Python library that makes it easy to parse HTML and XML documents.

### Creating BS4 Objects

- `bs4.BeautifulSoup()` function accepts a string containing the HTML it will parse, then returns a `BeautifulSoup object`

```python
import requests, bs4
res = requests.get('https://autbor.com/example3.html') # use requests.get() to download the main page as a string 
res.raise_for_status() # check for any issues downloading
example_soup = bs4.BeautifulSoup(res.text, 'html.parser') # create a BeautifulSoup object, html.parser is the default parser, says it's HTML style
print(type(example_soup)) # <class 'bs4.BeautifulSoup'>
```

- You can also load the HTML file from hard drive by passing `File object` to `bs4.BeautifulSoup()` function

```python 
# make sure you have html in your CWD
import bs4
with open('example3.html') and example_file: # open the file as a file object
	example_soup = bs4.BeautifulSoup(example_file, 'html.parser') # create a BeautifulSoup object
print(type(example_soup)) # <class 'bs4.BeautifulSoup'>
```

- Once we have a BeautifulSoup object, we can use it to find specific HTML elements

### Finding HTML Elements with BeautifulSoup

- You can retrieve web page element from BeautifulSoup object using `select()` method and pass it CSS selector string for the element you're looking for
- Method will return a `tag` objects which will represent matching HTML elements
- Examples of most common CSS selector patterns using select() method:
```python 
soup.select('div') # all <div> elements
soup.select('p') # all <p> elements
soup.select('div p') # all <p> elements inside <div> elements
soup.select('#author') # the <p> element with id="author"
soup.select('.notice') # all <p> elements with class="notice"
soup.select('div span') # all <span> elements inside <div> elements
soup.select('div > span') # all <span> elements that are direct children of <div> elements
soup.select('input[name]') # all <input> elements with a name attribute
soup.select('input[type="button"]') # all <input> elements with type="button"
```
- You can combine various selector patterns to make sophisticated matches.

for example:

```python
soup.select('p #author') # all <p> elements that contain an element with id="author"
```

- You can also pass `tag values` to `str() function` to show the HTML tags they represent
- `Tag values` also have `attrs` attribute containing all their HTML attributes as a dictionary.

```python
# Make sure to have example3.html in your CWD
import bs4
example_file = open('example3.html') # open the file as a file object
example_soup = bs4.BeautifulSoup(example_file.read(), 'html.parser') # create a BeautifulSoup object
elems = example_soup.select('#author') # find all elements with id="author"

print(type(elems)) # <class 'bs4.element.ResultSet'> - elems is a list of Tag objects
print(len(elems)) # 1
print(type(elems[0])) # <class 'bs4.element.Tag'> - this is a Tag object
print(str(elems[0].get_text())) # '<span id="author">Al Sweigart</span>' - this is the Tag object as a string
print(elems[0].get_text()) # 'Al Sweigart' - The inner text of the element
print(elems[0].attrs) # {'id': 'author'} - the attributes of the element
```

- This code finds the element with id="author" in our example HTML. 
	- use `select('#author')` to return a `list of all the elements with id="author"`
	- store this list of Tag objects in the variable `elems`. 
	- `len(elems)` tells us there is one `Tag object` in the `list`
	- Passing the `elems` to `str()` returns a string with the starting and closing tags and the element’s text.
	- `get_text()` on the `elems` returns the element’s text, or the content between the opening and closing tags
	- `attrs` returns a `dictionary with the element’s attribute`, 'id', and the value of the id attribute, 'author'

- You can also pull all the `<p>` elements from the BeautifulSoup object

```python
p_elems = example_soup.select('p') # find all <p> elements and store them in p_elems
print(str(p_elems[0])) # '<p>This <p> tag puts <b>content</b> into a <i>single</i> paragraph.</p>'
print(p_elems[0].get_text()) # 'This <p> tag puts content into a single paragraph.'

print(str(p_elems[1])) # '<p> <a href="https://inventwithpython.com/" >This text is a link</a> to books by <span id="author">Al Sweigart</span></p>'
print(p_elems[1].get_text()) # 'This text is a link to books by Al Sweigart.'

print(str(p_elems[2])) # '<p><img alt="Close-up of my cat Zophie." src="wow_such_zophie_thumb.webp"/></p>'
print(p_elems[2].get_text()) #
```

- `select()` gives us a list of three matches, which we store in `p_elems`
- Using str() on p_elems[0], p_elems[1], and p_elems[2] shows each element as a string
- using get_text() on each element shows it's text.

### Getting Data from an Element’s Attributes

- `get()` method for `Tag objects` allows us to access HTML attribute values from an element.
- pass the method an attribute name as a string to get the value of that attribute as a string

```python
# using example3.html
import bs4
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser') # create a BeautifulSoup object with a string of HTML code
span_elem = soup.select('span')[0] # find the first <span> element and store it in span_elem 

print(str(span_elem)) # '<span id="author">Al Sweigart</span>' - this is the element as a string
print(span_elem.get('id')) # 'author' - this is the value of the id attribute
print(span_elem.get('some_nonexistent_address') == None) # True - this attribute doesn't exist
print(span_elem.attrs) # {'id': 'author'} - those are the attributes of the element
```

- use `select()` to find any `<span>` elements and then store the first matched element in `span_elem`
- Passing the attribute name `'id'` to `get()` returns the attribute’s value: `'author'`

## Selenium module

- Selenium is a tool for automating web browsers
- [Docs](https://selenium-python.readthedocs.io/)
- needs to be installed: `pip install selenium`
- instead of importing the module we use `from selenium import webdriver`
- Selenium supports:
    - FireFox `webdriver.Firefox()`
    - Chrome `webdriver.Chrome()` 
    - Edge `webdriver.Edge()`
    - Safari `webdriver.Safari()`
    - Internet Explorer `webdriver.Ie()`

- Starting Selenium-controlled browser:
```python
from selenium import webdriver
browser = webdriver.Chrome()
type(browser) # <class 'selenium.webdriver.chrome.webdriver.WebDriver'>
browser.get('https://inventwithpython.com/') # open a page in the browser
```

### Browser buttons

- Selenium can simulate the user clicking the browser’s back, forward, refresh, and quit buttons
- `browser.back()` - goes back to the previous page
- `browser.forward()` - goes forward to the next page
- `browser.refresh()` - refreshes the page
- `browser.quit()` - closes the browser

### Finding Elements on the Page

- The **WebDriver object** has the `find_element()` method and `find_elements()` methods to find elements on the page.
    
    - `find_element()` returns the **first element** that matches the CSS selector.
        
    - `find_elements()` returns a **list of all elements** that match the CSS selector.
        
    - The results of `find_element()` and `find_elements()` are `WebElement` objects**.
        
- Selenium can find elements on the page using CSS selectors, class names, or IDs and store them in a `By` object.
    
    - To get the `By` object, first run `from selenium.webdriver.common.by import By`.
        
    - You can then pass it to `find_element()` or `find_elements()`.
        
- **Key Fact:** If no elements exist on the page that match what the method is looking for, Selenium will raise `NoSuchElementException`**.
    

---

### `WebElement` Attributes and Methods

|**Attribute/Method**|**Description**|**Example/Return Type**|
|---|---|---|
|`tag_name`|The tag name of the element.|`a` for an `<a element>`|
|`get_attribute(name)`|Returns the value of the attribute named `name`.|`href` in an `<a>` element|
|`get_property(name)`|Returns the value of the property named `name`.|`innerHTML` in an `<a>` element|
|`text`|The text inside the element.|`'hello'` in `<span>hello</span>`|
|`clear()`|Clears the text inside the text field or text area.|`None` (performs action)|
|`is_displayed()`|Returns `True` if the element is visible.|`Boolean`|
|`is_enabled()`|Returns `True` if the element is enabled.|`Boolean`|
|`is_selected()`|Returns `True` if the element is selected.|`Boolean`|
|`location`|The location of the element on the page.|`{'x': 100, 'y': 200}`|
|`size`|The size of the element.|`{'width': 100, 'height': 200}`|

---

### Selenium’s `By` Constants for Finding Elements

- `By.CLASS_NAME`**: Elements that use the CSS class `name`.
    
- `By.CSS_SELECTOR`**: Elements that match the CSS `selector`.
    
- `By.ID`**: Elements with a matching `id` attribute value.
    
- `By.LINK_TEXT`**: `<a>` elements that **completely** match the text provided.
    
- `By.PARTIAL_LINK_TEXT`**: `<a>` elements that **contain** the text provided.
    
- `By.NAME`**: Elements with a matching `name` attribute value.
    
- `By.TAG_NAME`**: Elements with a matching `tag name` (case-insensitive).

### Clicking Elements on the Page

- `FindElement` and `FindElements` returns a `WebElement`, which have a `click()` method that simulates a mouse click on the element.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://autbor.com/example3.html')

link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
print(type(link_elem))
# <class 'selenium.webdriver.remote.webelement.WebElement'>
link_elem.click() # follows the 'This text is a link' link and clicks on it
```

### Filling out and Submitting Forms

- first we need to find `<input>` or `<textarea>` elements for that text feld.
- then we call `send_keys()` on the element to fill it out.
- finally, we call `submit()` to send the form.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() # using Chrome
browser.get('https://autbor.com/example3.html')

user_elem = browser.find_element(By.ID, 'login_user') # find the login field
user_elem.send_keys('your_real_username_here') # enter the username

password_elem = browser.find_element(By.ID, 'login_pass') # find the pw field
password_elem.send_keys('your real password here') # fill in the password

password_elem.submit() # send the form
```

- This should work as long as website hasn't changed the ID of the username and password fields.

#### !!! Avoid putting passwords in source code, it's a bad idea and can leak them if they're unencrypted.

### Sending Special Keys

- module `selenium.webdriver.common.keys` contains all keyboard keys in attributes of the `Keys` class.
	- because of such a long name we usually import at the top of the file `from selenium.webdriver.common.keys import Keys`

- You can pass the `send_keys()` method any of the following constants from the `Keys` class to simulate pressing special keyboard keys:

| **Key Type** | **Constant** | **Description** |
| :--- | :--- | :--- |
| **Navigation** | `Keys.HOME` | Moves the cursor/view to the beginning of the line or page. |
| | `Keys.END` | Moves the cursor/view to the end of the line or page. |
| | `Keys.PAGE_UP` | Scrolls the page up. |
| | `Keys.PAGE_DOWN` | Scrolls the page down. |
| **Arrows** | `Keys.UP` | Up arrow key. |
| | `Keys.DOWN` | Down arrow key. |
| | `Keys.LEFT` | Left arrow key. |
| | `Keys.RIGHT` | Right arrow key. |
| **Action** | `Keys.ENTER` | The Enter key. |
| | `Keys.RETURN` | An alias for `Keys.ENTER` (often used for consistency across OS). |
| | `Keys.TAB` | The Tab key. |
| | `Keys.ESCAPE` | The Escape key. |
| **Editing** | `Keys.BACK_SPACE` | The Backspace key. |
| | `Keys.DELETE` | The Delete key. |
| **Function Keys** | `Keys.F1` to `Keys.F12` | Function keys F1 through F12 (e.g., `Keys.F5` for refresh). |

- You can also pass the method a string, for g. `'hello'` or `'?'`

- You can use `HOME` and `END` to move the cursor to the start and end of the line, respectively.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://autbor.com/example3.html')

html_elem = browser.find_element(By.TAG_NAME, 'html')
html_elem.send_keys(Keys.HOME) # moves the cursor to the start of the page
html_elem.send_keys(Keys.END) # moves the cursor to the end of the page
```

- a good place to send keys is to use the general `<HTML>` and `</HTML>` tag

- Selenium can do much more than what has been described here so far. 
	- It can modify cookies, take screenshot and run custom JS.
	- You can learn more here: [ReadTheDocs](https://selenium-python.readthedocs.io/)
	- And here: [Python Selenium talks](https://pyvideo.org)


## Playwright module

- [Docs](https://playwright.dev/python/)
- [Python conference talks](https://pyvideo.org/)

- Playwright is a modern browser automation library similar to Selenium
- the biggest `difference` is that Playwright is `headless`, meaning we don't need to actually open a browser window on the screen and it can just run in the background
- needs to be installed: `pip install playwright`
- instead of importing the module we use `from playwright.sync_api import sync_playwright`
- Playwright supports:
	 - Chrome, `playwright.chromium.launch()`
	 - Firefox `playwright.firefox.launch()`
	 - Edge `playwright.webkit.launch()`
	 - Safari `playwright.webkit.launch()`
	 - Internet Explorer `playwright.webkit.launch()`
- because of the close similarities CSS selector information can be referred to in [[Selenium]]


### Starting Playwright-controlled browser

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
	browser = playwright.chromium.launch() #  using chrome instead of ff
    page = browser.new_page() # open new page
    page.goto('https://autbor.com/example3.html') # go to the specified link
    print(page.title()) # prints the title of the page
    browser.close() # unlike in selenium, we need to close the browser manually
```

- Playwright automatically calls the `start()` and `stop()` methods when the `with` block is entered or exited
- It uses `synchronous` mode  - it's functions do not return until the operation is completed
    - it avoids for example looking for element before page finished loading
- By default it runs in headless mode, to turn it off use `browser = playwright.chromium.launch(headless=False, slow_mo=50)` to add 50ms delay between each action
    - this helps to debug any issues 

```python
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start() # start playwright
browser = playwright.chromium.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
# <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>
browser.close() # close the browser
playwright.stop() # stop playwright
```
- The `Page` object returned by `new_page()` is a new tab in a browser. You can have multiple tabs open at the same time.

### Clicking Browser buttons

- These methods are used on the `page` object in Playwright to simulate browser navigation actions.
| Method | Description |
| :--- | :--- |
| `page.go_back()` | Clicks the **Back** button, navigating to the previous page in history. |
| `page.go_forward()` | Clicks the **Forward** button, navigating to the next page in history. |
| `page.reload()` | Clicks the **Refresh/Reload** button, reloading the current page. |
| `page.close()` | Clicks the **Close Window** button, closing the current page/tab. |

### Finding elements on the page

- `Page` methods, called "locators" that return `Locator` objects - represent possible HTML elements ont he webpage
    - "possibly" because they are not guaranteed to be present on the page and may be raised later
    - Compared to `Selenium`, which would just throw an error, `Playwright` understands elements can be raised later
    - It will pause for 30s waiting for expected element to appear.
        - To avoid waiting 30s every time, you can use the `is_visible` method on the `Locator` object to check immediately if the element is present
        - Alternatively you can use `page.query_selector('selector')` method, where `selector` is a CSS or XPath selector. 
            - If it returns `None`, the element is not present on the page.

Playwright Locators for Finding Elements

| Locator Method | Targets/Description |
| :--- | :--- |
| `page.get_by_role(role, name=label)` | Elements by their **ARIA role** and optionally their accessible **label**. |
| `page.get_by_text(text)` | Elements that contain the specified `text` as part of their **inner text**. |
| `page.get_by_label(label)` | Elements associated with matching `<label>` text. |
| `page.get_by_placeholder(text)` | `<input>` and `<textarea>` elements with matching `placeholder` attribute values. |
| `page.get_by_alt_text(text)` | `<img>` elements with matching `alt` attribute values. |
| `page.locator(selector)` | Elements matching a generic **CSS or XPath selector**. |

* ARIA Standard defines roles (like button, link, checkbox, heading) that describe the purpose of an element to assistive technologies like screen readers.
* `alt` attribute is a text description of the element for users who cannot see it.
* **Best Practice:** Prioritize accessibility locators (`get_by_role`, `get_by_text`, `get_by_label`) for robust tests.

* `page.locator(selector)` is the general-purpose, but often less resilient, selector.
* It's similar to selenium's find_elements() method.


|Method | Description |
| :--- | :--- |
| `get_attribute(name)` | Returns the value for the element’s `name` attribute (e.g., 'https://nostarch.com' for the `href` attribute). |
| `count()` | Returns an **integer** representing the number of matching elements in this `Locator` object. |
| `nth(index)` | Returns a `Locator` object for the matching element at the specified **zero-based index** (e.g., nth(3) returns the fourth element). |
| `first` | The `Locator` object of the **first** matching element (equivalent to nth(0)). |
| `last` | The `Locator` object of the **last** matching element (e.g., for five elements, this is equivalent to nth(4)). |
| `all()` | Returns a list of `Locator` objects for **each individual** matching element. |
| `inner_text()` | Returns the `text` content **within** the element (e.g., 'hello' in `<b>hello</b>`). |
| `inner_html()` | Returns the `HTML` source within the element (e.g., `<b>hello</b>` in `<b>hello</b>`)." |
| `click()` | Simulates a **mouse click** on the element, useful for links, checkboxes, and buttons. |
| `is_visible()` | Returns `True` if the element is **visible**; otherwise, returns `False`. |
| `is_enabled()` | For input elements, returns `True` if the element is **enabled**; otherwise, returns `False`. |
| `is_checked()` | For checkbox or radio button elements, returns `True` if the element is **selected/checked**; otherwise, returns `False`. |
| `bounding_box()` | Returns a **dictionary** with element position `(x, y)` and size `(width, height)`. |

#### Obtaining single locator object

- `Locator` objects can represent multiple elements.
- To obtain **individual** `locator` object, use the `nth()` method and pass it a **zero-based** index.
- To obtain a **list** of `locator` objects, use the `all()` method.

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('https://autbor.com/example3.html')

    elems = page.locator('p') # find all <p> elements and store them in elems
    print(elems.nth(0).inner_text()) 
    # This <p> tag puts content into a single paragraph.
    print(elems.nth(0).inner_html())
    # This &lt;p&gt; tag puts <b>content</b> into a <i>single</i> paragraph.
```

### Clicking elements on the page

- `Page` object has `click()`, `check()`, `uncheck()` and `set_checked()` methods to interact with elements.
- You can call those methods and pass the string of a CSS or XPath `selector` of the element you want to interact with
- OR you can use Playwright's `locator` functions to obtain a `locator` object and call the `click()` method on it.

```python
from playwright.sync_api import sync_playwright
playwright = sync_playwright().start() # start playwright
browser = playwright.chromium.launch(headless=False, slow_mo=500) # open browser in NON-headless mode
page = browser.new_page() # open new page
page.goto('https://autbor.com/example3.html') # go to the specified link
# <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>
page.click('input[type="checkbox"]') # check the checkbox
page.click('input[type="checkbox"]') # uncheck the checkbox
page.click('a') # click the link
page.go_back() # go back to the previous page

checkbox_elem = page.get_by_role('checkbox') # get the checkbox element using Locator method
checkbox_elem.check() # check the checkbox
checkbox_elem.uncheck() # uncheck the checkbox

checkbox_elem.set_checked(True) # check the checkbox
checkbox_elem.set_checked(False) # uncheck the checkbox

page.get_by_text('is a link').click() # click the link with text "is a link"

browser.close() # close the browser
playwright.stop() # stop playwright
```

### filling out and submitting the forms

- `locator` objects have `fill()` method to fill out text fields such as `<input>` or `<textarea>`.
- there is also `clear()` method to clear the field in case there is placeholder text already there.

```python
from playwright.sync_api import sync_playwright
playwright = sync_playwright().start() # start playwright
browser = playwright.chromium.launch(headless=False, slow_mo=500) # open browser in NON-headless mode
page = browser.new_page() # open new page
page.goto('https://autbor.com/example3.html') # go to the specified link
# <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>

page.locator('#login_user').fill('Your_real_username') # fill in the username field with your real username
page.locator('#login_pass').fill('Your_real_password') # fill in the password field with your real password
page.locator('input[type=submit]').click() # click the submit button

browser.close() # close the browser
playwright.stop() # stop playwright
```
### Sending Special keys

- You can also simulate keyboard key presses on `elements` in the web page with the `press()` method for `Locator` objects

```python
from playwright.sync_api import sync_playwright
playwright = sync_playwright().start() # start playwright
browser = playwright.chromium.launch(headless=False, slow_mo=500) # open browser in NON-headless mode
page = browser.new_page() # open new page
page.goto('https://autbor.com/example3.html') # go to the specified link
# <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>

page.locator('html').press('End') # move the cursor to the end of the page
page.locator('html').press('Home') # move the cursor to the beginning of the page

browser.close() # close the browser
playwright.stop() # stop playwright
```

- The strings you pass to press() can include:
 - single character strings (such as 'a' or '?'); 
 - the modification keys 'Shift', 'Control', 'Alt', 
 - `'Meta'` (as in `'Control+A'`, for `CTRL-A`); 
 - and any of the following:
 
| Key Code | Description |
| :--- | :--- |
| **Backquote** | Tilde (~) / Backtick (`) key. |
| **Minus** | Hyphen (-) / Underscore (_) key. |
| **Equal** | Equals (=) / Plus (+) key. |
| **Backslash** | Backslash (\) / Pipe (|) key. |
| **Backspace** | Deletes the character before the cursor. |
| **Tab** | Moves focus or inserts a tab character. |
| **Delete** | Deletes the character after the cursor. |
| **Escape** | General purpose cancel/exit key. |
| **Enter** | Submits a form or confirms an action. |
| **Insert** | Toggles insert/overwrite mode. |
| **End** | Moves the cursor to the end of a line or document. |
| **Home** | Moves the cursor to the start of a line or document. |
| **PageUp** | Scrolls one page up in content. |
| **PageDown** | Scrolls one page down in content. |
| **ArrowDown** | Moves the cursor or scrolls down. |
| **ArrowRight** | Moves the cursor right. |
| **ArrowUp** | Moves the cursor or scrolls up. |
| **F1 to F12** | Programmable function keys. |
| **Digit0 to Digit9** | Numerical digit keys (0 through 9). |
| **KeyA to KeyZ** | Alphabetical letter keys (A through Z). |


