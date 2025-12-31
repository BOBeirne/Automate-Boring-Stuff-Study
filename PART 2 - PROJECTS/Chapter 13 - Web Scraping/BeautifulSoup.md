
# BeautifulSoup

- Documentation can be found [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Requires to be installed with `pip install beautifulsoup4` , `bs4` to import
- BeautifulSoup is a Python library that makes it easy to parse HTML and XML documents.

## Creating BS4 Objects

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

## Finding HTML Elements with BeautifulSoup

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

## Getting Data from an Element’s Attributes

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
