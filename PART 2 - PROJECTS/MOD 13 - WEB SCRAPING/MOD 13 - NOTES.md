## Modules used in this chapter

- webbrowser - built-in python browser that opens to specific page - see project file
- requests - downloads files and web pages from internet
- BeautifulSoup (bs4) - parses downloaded html file to extract the info you're looking for
- Selenium - launches and controls the webbrowser (filling in forms, simulating mouse clicks)
- json - used to parse json files

## Downloading Web Pages

### requests module

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

#### Checking for errors

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

#### Saving Downloaded Files to the Hard Drive

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

### API

- [[API]] - Application Programming Interface
	- specification that defines how one piece of software (eg. Python program) can communicate with another piece of software (eg. web server with weather information)
	- even if API is free almost all online service will require registration. You can use temp e-mail service like [10minuteemail.com](https://10minuteemail.com/)
	- Many HTTP APIs deliver their responses as one large string. This string is often formatted as JSON or XML. 
	- `json.loads(response.text)` returns a Python data structure of lists and dictionaries containing the JSON data in response.text.


#### Breaking down the API URL formatting

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


#### Using the API

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

#### Finding temperature of San Francisco

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

#### Requesting a Latitude and Longitude

- Endpoint: `https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}`
- If OpenWeather is unable to locate the city, response_data will be an empty list.
- If the city name matches multiple responses, the list in response_data will contain different dictionaries at response_data[0], response_data[1], and so on.

```python
import requests, json
response_data[0]['lat'] # returns latitude as a float
response_data[0]['lon'] # returns longitude as a float
```	

#### Fetching the Current Weather

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

#### Getting a Weather Forecast

Endpoint for 5-day forecast is `https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}`

```python
response_data['list'] # Holds a list of dictionaries containing the weather predictions for a given time.
response_data['list'][0]['dt'] # Holds a timestamp in the form of a Unix epoch float. Pass this value as an argument to datetime.datetime.fromtimestamp() to obtain the timestamp as a datetime object.
response_data['list'][0]['main'] # Holds a dictionary with keys like 'temp', 'feels_like', 'humidity', and others.
response_data['list'][0]['weather'][0] # Holds a dictionary of descriptions with keys like 'main', 'description', and others.
```

### HTML

- Use of webscraping requires at least basic knowledge of HTML and CSS
- you can learn more about HTML here
	- [Mozilla HTML docs](https://developer.mozilla.org/en-US/docs/Learn/HTML)
	- [FreeCodeCamp](https://www.freecodecamp.org/news/html-coding-introduction-course-for-beginners)
	- [Khan Academy](https://www.khanacademy.org/computing/computer-programming/html-css)

- Some HTML elements have an `id` attribute used to uniquely identify the element in the page. You’ll often instruct your programs to seek out an element by its id attribute, so finding this attribute using the browser’s Developer Tools is a common task when writing web scraping programs.

#### Viewing a Web Page’s Source Code

- To see page's HTML code right-click any web page in your web browser (or CTRL-click it on macOS), and select View Source or View page source
- It’s fine if you don’t fully understand what you’re seeing. You just need enough knowledge to pick out data from an existing site.

#### Web Browser Developer Tools

- Press F12 to make the toolbar appear
- Pressing F12 again will make it disappear.
- Right-click any part of the web page and select Inspect Element from the context menu to bring up the HTML responsible for that part of the page. This will help you parse HTML for your web scraping programs.

#### **DO NOT** USE REGEX WITH HTML PARSING

Locating a specific piece of HTML (or a piece of XML, JSON, TOML, or YAML) in a string seems like a perfect case for regular expressions. The advice is not to do this. 
HTML can be formatted in many ways and still be considered valid, but trying to capture all these possible variations in a regular expression is tedious and error prone. 

Using a module developed specifically for parsing HTML, such as bs4, is less likely to result in bugs.
You can find an extended argument for why you shouldn’t parse HTML with regular expressions at https://stackoverflow.com/a/1732454/1893164.

#### Finding HTML Elements

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

