# Selenium module

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

| **Attribute/Method**  | **Description**                                     | **Example/Return Type**           |
| --------------------- | --------------------------------------------------- | --------------------------------- |
| `tag_name`            | The tag name of the element.                        | `a` for an `<a element>`          |
| `get_attribute(name)` | Returns the value of the attribute named `name`.    | `href` in an `<a>` element        |
| `get_property(name)`  | Returns the value of the property named `name`.     | `innerHTML` in an `<a>` element   |
| `text`                | The text inside the element.                        | `'hello'` in `<span>hello</span>` |
| `clear()`             | Clears the text inside the text field or text area. | `None` (performs action)          |
| `is_displayed()`      | Returns `True` if the element is visible.           | `Boolean`                         |
| `is_enabled()`        | Returns `True` if the element is enabled.           | `Boolean`                         |
| `is_selected()`       | Returns `True` if the element is selected.          | `Boolean`                         |
| `location`            | The location of the element on the page.            | `{'x': 100, 'y': 200}`            |
| `size`                | The size of the element.                            | `{'width': 100, 'height': 200}`   |

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

| **Key Type**      | **Constant**            | **Description**                                                   |
| :---------------- | :---------------------- | :---------------------------------------------------------------- |
| **Navigation**    | `Keys.HOME`             | Moves the cursor/view to the beginning of the line or page.       |
|                   | `Keys.END`              | Moves the cursor/view to the end of the line or page.             |
|                   | `Keys.PAGE_UP`          | Scrolls the page up.                                              |
|                   | `Keys.PAGE_DOWN`        | Scrolls the page down.                                            |
| **Arrows**        | `Keys.UP`               | Up arrow key.                                                     |
|                   | `Keys.DOWN`             | Down arrow key.                                                   |
|                   | `Keys.LEFT`             | Left arrow key.                                                   |
|                   | `Keys.RIGHT`            | Right arrow key.                                                  |
| **Action**        | `Keys.ENTER`            | The Enter key.                                                    |
|                   | `Keys.RETURN`           | An alias for `Keys.ENTER` (often used for consistency across OS). |
|                   | `Keys.TAB`              | The Tab key.                                                      |
|                   | `Keys.ESCAPE`           | The Escape key.                                                   |
| **Editing**       | `Keys.BACK_SPACE`       | The Backspace key.                                                |
|                   | `Keys.DELETE`           | The Delete key.                                                   |
| **Function Keys** | `Keys.F1` to `Keys.F12` | Function keys F1 through F12 (e.g., `Keys.F5` for refresh).       |

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
