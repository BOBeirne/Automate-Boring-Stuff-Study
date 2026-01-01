# HTML

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
	- You can pass it to Beautiful Soup’s select() method [[BeautifulSoup]]
	- or Selenium’s find_element() method [[selenium]]
- CSS selector syntax used in this string specifies which HTML elements to retrieve from a web page

#### when a website changes its layout, you’ll need to update the HTML tags your scripts check. Be sure to keep an eye on your program in case it suddenly displays errors about not being able to find elements.

Parsing HTML with BeautifulSoup -> [[BeautifulSoup]]