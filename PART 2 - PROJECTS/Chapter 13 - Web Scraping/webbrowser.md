# webbrowser module

- [documentation](https://docs.python.org/3/library/webbrowser.html)

## CLI

- `webbrowser` can be used as a command-line interface for the module. 
- It accepts a URL as the argument and the following optional parameters:
  - `-n, --new-window` - Opens the URL in a new browser window, if possible.
  - `-t, --new-tab` - Opens the URL in a new browser tab.
- The options are, mutually exclusive.

example:
`python -m webbrowser -t "https://www.python.org"`


## Exceptions

exception webbrowser.Error is: `exception webbrowser.Error`

## functions

- `webbrowser.open_new(url)` - **Open** url in a **new window of the default browser**, if possible, otherwise, open url in the only browser window.
	- Returns `True` if a browser was successfully launched, False otherwise.

- `webbrowser.open_new_tab(url)` - **Open** url in a **new page (“tab”) of the default browser**, if possible, otherwise equivalent to open_new().
  - Returns `True` if a browser was successfully launched, False otherwise.

- `webbrowser.get(using=None)` - **Return a controller object for the browser type** using. 
  - If using is `None`, **return a controller for a default browser** appropriate to the caller’s environment.

- `webbrowser.register(name, constructor, instance=None, *, preferred=False)` - **Register the browser type name**. 
  - Once a browser type is registered, the `get()` function can return a controller for that browser type. 
  - If instance is not provided, or is None, constructor will be called without parameters to create an instance when needed. 
  - If instance is provided, constructor will never be called, and may be None.

**Setting preferred to True** makes this browser a preferred result for a `get() call` with **no argument**. Otherwise, this entry point is only useful if you plan to either set the `BROWSER` variable or call `get()` with a nonempty argument matching the name of a handler you declare.


## Open new tab or window

```python
url = 'https://docs.python.org/'

webbrowser.open_new_tab(url) # Open URL in a new tab, if a browser window is already open.
webbrowser.open_new(url) # Open URL in new window, raising the window if possible.
```

## Browser controller objects

- `Browser controllers` provide the `name attribute`, and the following **three methods** which parallel module-level convenience functions:
- `controller.name`
- where `name` is the System-dependent **name for the browser**.


`controller.open(url, new=0, autoraise=True)`
Display url using the browser handled by this controller. If new is 1, a new browser window is opened if possible. If new is 2, a new browser page (“tab”) is opened if possible.

`controller.open_new(url)`
Open url in a new window of the browser handled by this controller, if possible, otherwise, open url in the only browser window. Alias open_new().

`controller.open_new_tab(url)`
Open url in a new page (“tab”) of the browser handled by this controller, if possible, otherwise equivalent to open_new().