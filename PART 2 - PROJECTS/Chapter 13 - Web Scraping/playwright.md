# Playwright module

- [Docs](https://playwright.dev/python/)
- [Python conference talks](https://pyvideo.org/)

- `Playwright` is a **modern browser automation library similar to Selenium**
- the biggest **difference** is that Playwright is `headless`, meaning we don't need to actually open a browser window on the screen and it can just run in the background
- install: `pip install playwright`
- import: `from playwright.sync_api import sync_playwright`
- Playwright **supports**:
	 - **Chrome**, `playwright.chromium.launch()`
	 - **Firefox** `playwright.firefox.launch()`
	 - **Edge** `playwright.webkit.launch()`
	 - **Safari** `playwright.webkit.launch()`
	 - **Internet Explorer** `playwright.webkit.launch()`

- because of the **close similarities CSS selector** information can be referred to in [[Selenium]]


## Starting Playwright-controlled browser

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

## Clicking Browser buttons

- These methods are used on the `page` object in Playwright to simulate browser navigation actions.
| Method              | Description                                                             |
| :------------------ | :---------------------------------------------------------------------- |
| `page.go_back()`    | Clicks the **Back** button, navigating to the previous page in history. |
| `page.go_forward()` | Clicks the **Forward** button, navigating to the next page in history.  |
| `page.reload()`     | Clicks the **Refresh/Reload** button, reloading the current page.       |
| `page.close()`      | Clicks the **Close Window** button, closing the current page/tab.       |

## Finding elements on the page

- `Page` methods, called "locators" that return `Locator` objects - represent possible HTML elements ont he webpage
    - "possibly" because they are not guaranteed to be present on the page and may be raised later
    - Compared to `Selenium`, which would just throw an error, `Playwright` understands elements can be raised later
    - It will pause for 30s waiting for expected element to appear.
        - To avoid waiting 30s every time, you can use the `is_visible` method on the `Locator` object to check immediately if the element is present
        - Alternatively you can use `page.query_selector('selector')` method, where `selector` is a CSS or XPath selector. 
            - If it returns `None`, the element is not present on the page.

Playwright Locators for Finding Elements

| Locator Method                       | Targets/Description                                                               |
| :----------------------------------- | :-------------------------------------------------------------------------------- |
| `page.get_by_role(role, name=label)` | Elements by their **ARIA role** and optionally their accessible **label**.        |
| `page.get_by_text(text)`             | Elements that contain the specified `text` as part of their **inner text**.       |
| `page.get_by_label(label)`           | Elements associated with matching `<label>` text.                                 |
| `page.get_by_placeholder(text)`      | `<input>` and `<textarea>` elements with matching `placeholder` attribute values. |
| `page.get_by_alt_text(text)`         | `<img>` elements with matching `alt` attribute values.                            |
| `page.locator(selector)`             | Elements matching a generic **CSS or XPath selector**.                            |

* ARIA Standard defines roles (like button, link, checkbox, heading) that describe the purpose of an element to assistive technologies like screen readers.
* `alt` attribute is a text description of the element for users who cannot see it.
* **Best Practice:** Prioritize accessibility locators (`get_by_role`, `get_by_text`, `get_by_label`) for robust tests.

* `page.locator(selector)` is the general-purpose, but often less resilient, selector.
* It's similar to selenium's find_elements() method.


| Method                | Description                                                                                                                          |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `get_attribute(name)` | Returns the value for the element’s `name` attribute (e.g., 'https://nostarch.com' for the `href` attribute).                        |
| `count()`             | Returns an **integer** representing the number of matching elements in this `Locator` object.                                        |
| `nth(index)`          | Returns a `Locator` object for the matching element at the specified **zero-based index** (e.g., nth(3) returns the fourth element). |
| `first`               | The `Locator` object of the **first** matching element (equivalent to nth(0)).                                                       |
| `last`                | The `Locator` object of the **last** matching element (e.g., for five elements, this is equivalent to nth(4)).                       |
| `all()`               | Returns a list of `Locator` objects for **each individual** matching element.                                                        |
| `inner_text()`        | Returns the `text` content **within** the element (e.g., 'hello' in `<b>hello</b>`).                                                 |
| `inner_html()`        | Returns the `HTML` source within the element (e.g., `<b>hello</b>` in `<b>hello</b>`)."                                              |
| `click()`             | Simulates a **mouse click** on the element, useful for links, checkboxes, and buttons.                                               |
| `is_visible()`        | Returns `True` if the element is **visible**; otherwise, returns `False`.                                                            |
| `is_enabled()`        | For input elements, returns `True` if the element is **enabled**; otherwise, returns `False`.                                        |
| `is_checked()`        | For checkbox or radio button elements, returns `True` if the element is **selected/checked**; otherwise, returns `False`.            |
| `bounding_box()`      | Returns a **dictionary** with element position `(x, y)` and size `(width, height)`.                                                  |

### Obtaining single locator object

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

## Clicking elements on the page

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

## filling out and submitting the forms

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
## Sending Special keys

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
 
| Key Code             | Description                                          |
| :------------------- | :--------------------------------------------------- |
| **Backquote**        | Tilde (~) / Backtick (`) key.                        |
| **Minus**            | Hyphen (-) / Underscore (_) key.                     |
| **Equal**            | Equals (=) / Plus (+) key.                           |
| **Backslash**        | Backslash (\) / Pipe (                               | ) key. |
| **Backspace**        | Deletes the character before the cursor.             |
| **Tab**              | Moves focus or inserts a tab character.              |
| **Delete**           | Deletes the character after the cursor.              |
| **Escape**           | General purpose cancel/exit key.                     |
| **Enter**            | Submits a form or confirms an action.                |
| **Insert**           | Toggles insert/overwrite mode.                       |
| **End**              | Moves the cursor to the end of a line or document.   |
| **Home**             | Moves the cursor to the start of a line or document. |
| **PageUp**           | Scrolls one page up in content.                      |
| **PageDown**         | Scrolls one page down in content.                    |
| **ArrowDown**        | Moves the cursor or scrolls down.                    |
| **ArrowRight**       | Moves the cursor right.                              |
| **ArrowUp**          | Moves the cursor or scrolls up.                      |
| **F1 to F12**        | Programmable function keys.                          |
| **Digit0 to Digit9** | Numerical digit keys (0 through 9).                  |
| **KeyA to KeyZ**     | Alphabetical letter keys (A through Z).              |
