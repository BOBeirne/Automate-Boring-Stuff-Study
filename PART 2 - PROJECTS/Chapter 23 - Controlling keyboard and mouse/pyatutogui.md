# PyAutoGUI

- Module used for GUI automation
- Install using `pip install pyautogui`
- Import using `pyautogui`
- [Docs](https://pyautogui.readthedocs.io/) 
- Do not EVER save programs as `pyautogui.py` - python will think your program is a module
- Only supports main monitor, no current support for multi-monitor setup.

## Fail Safes

- To exit the program using PyAutoGUI, quickly move your mouse to one of the corners of the screen
  - This will raise `pyautogui.FailSafeException`
  - To disable this fail-safe, set `pyautogui.FAILSAFE` to `False`. **DISABLING FAIL-SAFE IS NOT RECOMMENDED.**
- You can adjust how often program executes an action using `pyautogui.PAUSE` and setting itmore than to default `0.1` seconds
- Windows & Linux `CTRL + ALT + DEL` also works to exit the program, 
- macOS version: `mac + shift + Q`

## macOS

- Mac OS doesn't usually allow programs control Keyboard or mouse
- In order to override this security feature, PyAutoGUI must be set as an accessibility application.
  - 1 - Open the IDE application
  - 2 - goto `System Preferences` -> `accessibility tab`
  - 3 - Check the IDE application checkbox
  - 4 - provide your password to confirm changes

## Basics

- `PyAutoGUI` uses `x` and `y` coordinates, just like `PIL` 
- `(0,0)` = `(x,y)` - is the top-left corner and `x` increases to the right (horizontal coordinate), while `y` increases downwards (vertical)
- for screen **resolution** of `1920×1080` the eah corner will be:
  - top-left: (0,0)
  - top-right: (1920,0)
  - bottom-left: (0,1080)
  - bottom-right: (1920,1080)

## size()

- To get screen size, use `pyautogui.size()` function

```python
import pyautogui
screen_size = pyautogui.size() # get resolution
print(screen_size)
# Size(width=1920, height=1080)
screen_size.width
# 1920
screen_size.height
# 1080
tuple(screen_size)
# (1920, 1080)
```

## moveTo()

- `pyautogui.moveTo(x, y)` - moves mouse to the specified location
- It has an optional `duration` argument, eg. `pyautogui.moveTo(100, 100, duration=0.25)` , the default is `0` if left empty

```python
import pyautogui
for i in range(10):  # Move the mouse in a square.
	pyautogui.moveTo(100, 100, duration=0.25)
	pyautogui.moveTo(200, 100, duration=0.25)
	pyautogui.moveTo(200, 200, duration=0.25)
	pyautogui.moveTo(100, 200, duration=0.25)
```

## move()

- similar to `MoveTo()`, BUT, moves mouse RELATIVE to it's CURRENT position
- takes 3 arguments (x,y and optional delay)

```python
import pyautogui
for i in range(10):  # Move the mouse in a square.
	pyautogui.move(100, 0, duration=0.25)  # Right
	pyautogui.move(0, 100, duration=0.25)  # Down
	pyautogui.move(-100, 0, duration=0.25)  # Left
	pyautogui.move(0, -100, duration=0.25)  # Up
```

## position()

- Use this function to get the current xy of the `point` position of the mouse, at the time of the function call

```python
import pyautogui
pyautogui.position() # Get the current mouse position.
# Point(x=1367, y=972)
p = pyautogui.position() # Get the current mouse position again.
print(p)
# Point(x=1140, y=909)
p[0] # x-coordinate
# 1140
p.x # another way to get x coordinate
# 1140
p[1]
# 909
p.y
# 909
```

## click()

- A full “click” is defined as pushing a mouse button down and then releasing it without moving the cursor
- `pyautogui.click(x, y)` - clicks at the specified location
- if x,y are not specified takes place wherever the mouse currently is.
- by default, uses left button
- `pyautogui.click(button='right')` - click with right mouse button
  - alternative to `pyautogui.rightClick()`
- `pyautogui.click(button='middle')` - click with middle mouse button
  - alternative to `pyautogui.middleClick()`

```python
import pyautogui
pyautogui.click(10, 5)  # Move the mouse to (10, 5) and click.

pyautogui.click(active_win.left + 10, active_win.top + 20) # you can also use arithmetics
```

### mouseUP and mouseDown

- Only click by calling `pyautogui.mouseDown()`, which only pushes the mouse button down, without releasing it
- and `pyautogui.mouseUp()` only releases the button.
- `click()` function is actually a wrapper around the above 2 functions.

## doubleclick()

- performs a double click with a left mouse button

## dragTo()

- Dragging, means moving the mouse while holding down the mouse button
- there are 2 versions: `dragTo()` and `drag()`, which work the same as `moveTo()` and `move()`
- `pyautogui.dragTo(x, y)` - drags the mouse to the specified location on the xy screen coordinates
- while `pyautogui.drag()`, drags the mouse relative to it's current position.
- takes 3 arguments (x,y and optional delay)
  - macOS: need to use delay as otherwise it may cause incorrect behavior

Example:
- Use website [SumoPaint](https://sumopaint.com/)

```python
import pyautogui
pyautogui.sleep(5) # give you time to move mouse into the position
pyautogui.click()  # Click to make the window active.
distance = 300
change = 20

while distance > 0:
	pyautogui.drag(distance, 0, duration=0.2)  # move right.
	distance -= change
	pyautogui.drag(0, distance, duration=0.2)  # move down.
	pyautogui.drag(-distance, 0, duration=0.2)  # move left.
	distance -= change
	pyautogui.drag(0, -distance, duration=0.2)  # move up.
```

## sleep()

- `pyautogui.sleep(5)` - pauses execution for 5 seconds
- same as `time.sleep(5)`, built into the pyautogui module itself

## scroll()

- `pyautogui.scroll(100)` - scrolls the mouse wheel 100 times
  - positive int scrolls up, negative scrolls down
- the size of a scroll unit depends on your OS and/or computer configuration
- scrolling takes place at the mouse cursor position

## mouseInfo()

- [Docs](https://mouseinfo.readthedocs.io/)
- `pyautogui.mouseInfo()` is meant to be called from **shell** rather than inside the program
- remember, it only support 1, main monitor!
- launches a small mouseInfo application that is included in the module
- app provides the current mouse position as x and y and RGB color at the location
- Copy options usually have included 3 second delay (tick box) it can be disabled 

## screenshot()

- `pyautogui.screenshot()` - takes a screenshot of the entire screen
- `pyautogui.screenshot(region=(x,y,x,y))` - takes a screenshot of the specified region
- You can **pass it to a variable**, which will then hold the `Pillow image object` of a screenshot

## pixel()

- `pyautogui.pixel(x, y)` - returns the RGB color of the pixel at the specified location

```python
pyautogui.pixel(0, 0)
# (60, 60, 60)
pyautogui.pixel(50,200)
# (37, 37, 38)
```

### pixelMatchesColor()

- Returns `rue` if picel at `xy` coordinate matches the given color
- function takes 3 arguments:`pyautogui.pixelMatchesColor(x, y, (RGBcolorTuple))`
  - x
  - y
  - (R,G,B) tuple

```python
pyautogui.pixel(50,200)
# (37, 37, 38)
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
# False
pyautogui.pixelMatchesColor(50, 200, (37, 37, 38))
# True
```

## locateOnScreen()

- If you have taken for example a screenshot, you can use `pyautogui.locateOnScreen()` to find the location of an image on the screen by providing it an image as an argument
```python
import pyautogui
box = pyautogui.locateOnScreen('calculator.png')
print(box)
# Box(left=np.int64(1438), top=np.int64(269), width=308, height=484)
```

### ImageNotFoundException

- NOTE: As of version 0.9.41, if the locate functions can’t find the provided image, they’ll raise `ImageNotFoundException` instead of returning None. 
- [Source](https://pyautogui.readthedocs.io/en/latest/screenshot.html)
- Note that the image on the screen must match the provided image perfectly in order to be recognized
- if dealing with lower quality images, use optional `confidence` argument

### confidence

- The **optional `confidence` keyword argument** specifies the **accuracy** with which the function should locate the image on screen. This is helpful in case the function is not able to locate an image due to **negligible pixel differences**
  - Note: You need to have [OpenCV](https://docs.opencv.org/4.x/db/dd1/tutorial_py_pip_install.html) (Open Source Computer Vision) installed for the confidence keyword to work. 
  - usually via pip: `pip install opencv-python ` check docs for more options, 
  - may need to upgrade wheel first - `python -m pip install --upgrade pip setuptools wheel`
- On a 1920 x 1080 screen, the locate function calls take about 1 or 2 seconds. This may be too slow for action video games, but works for most purposes and applications.

```python
import pyautogui
box = pyautogui.locateOnScreen('calculator.png', confidence=0.9)
print(box)
# Box(left=np.int64(1438), top=np.int64(269), width=308, height=484)
```

## locateAllOnScreen()

- If there are multiple matches for the image, the function `locateAllOnScreen()` will return a `Generator object`
- Beyond scope of this book, [Python Generators - Visually Explained](https://www.youtube.com/watch?v=GWZf_B129zs)
- Can be passed to `list()` function to return a `list of generator objects`
  - There will be one box object per location

```python
list(pyautogui.locateAllOnScreen('x.png'))
# [Box(left=np.int64(679), top=np.int64(15), width=30, height=20), Box(left=np.int64(211), top=np.int64(16), width=30, height=20), Box(left=np.int64(445), top=np.int64(16), width=30, height=20)]
```

- Here we have 3 x boxes 
- Once you have the box, you can click it via coordinates

```python
pyautogui.click((679, 15, 30, 20))
# this will press x incon and close the window
```

- Or you can pass the image file too

```python
pyautogui.click('x.png')
# don't run it unless you want all windows closed :')
```

- You can also use `moveto()` and `dragto()` on image file adguments
- It will raise an exception fi it can't find the image on the screen

```python
try:
	loc = pyautogui.locateOnScreen('x.png')
except pyautogui.ImageNotFoundException:
    print('Image could not be found.')
```

## Window (Windows only)

- Works only on windows as of version 1.0.0
- Uses `PyGetWindow` package in `PyAutoGUI`

### Comparison of all window functions

| Function                             | Description                                                                                                |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `pyautogui.getActiveWindow() `         | Returns the **Window object for the currently active (focused) window.**                                       |
| `pyautogui.getAllWindows()`            | Returns a **list of Window objects for every visible window** on the screen.                                   |
| `pyautogui.getWindowsAt(x, y)`         | Returns a **list of Window objects for every visible window that includes the point** (x, y).                  |
| `pyautogui.getWindowsWithTitle(title)` | Returns a list of Window objects for **every visible window that includes the string title in its title bar**. |
| `pyautogui.getAllTitles()`             | Returns a list of **strings of every visible window**.                                                         |


### getActiveWindow()

- Used to obtain the active window
- Returns a `Window object`, which then can use to retrieve window attributes such as:
	- `left`, `right`, `top`, `bottom` - **single int** for the **x- or y-**coordinate of the **window’s side**
	- `topleft`, `topright`, `bottomleft`, `bottomright` -  **tuple** of **two ints** for the **(x, y) coordinate of the window’s corner**
	- `midleft`, `midright`, `midtop`, `midbottom` - **tuple** of **two ints** for the **(x, y) coordinate** of the **middle of the window’s sides**
	- `width`, `height`-  **single int** for one of the **window’s dimensions, in**
	- `size`- **tuple of two ints for the (width, height) of the window**
	- `area` - **single int** representing the **area** of the window, in
	- `centerx`, `centery `- A **single int for the x- or y-coordinate of the window’s center**
	- `box` - **tuple of four ints** for the (left, top, width, height) **measurements** of the window
	- `title` - **string** of the text in the **title bar** at the top of the window

```python
active_window = pyautogui.getActiveWindow()
active_window
# Win32Window(hWnd=269014)
str(active_window)
# '<Win32Window left="-8", top="-8", width="1936", height="1048", title="● pyatutogui.md - Automate boring stuff - Visual Studio Code">'
active_window.title
# '● pyatutogui.md - Automate boring stuff - Visual Studio Code'
active_window.size
# Size(width=1936, height=1048)
active_window.left, active_window.top, active_window.right, active_window.bottom
# (-8, -8, 1928, 1040)
active_window.topleft
# Point(x=-8, y=-8)
```

### Window object methods

| Method                    | Action                        | Return Value                                                  |
| ------------------------------- | ----------------------------- | ------------------------------------------------------------- |
| active_win.width                | Gets current width            | 1936 (int)                                                    |
| active_win.topleft              | Gets window position          | Point(x=174, y=153)                                           |
| active_win.width = 1000         | Sets/resizes width            | None (modifies in place)                                      |
| active_window.title             | Gets window title             | '● pyautogui.md - Automate boring stuff - Visual Studio Code' |
| active_window.size              | Gets window dimensions        | Size(width=1936, height=1048)                                 |
| active_window.left              | Gets left edge position       | -8 (int)                                                      |
| active_window.top               | Gets top edge position        | -8 (int)                                                      |
| active_window.right             | Gets right edge position      | 1928 (int)                                                    |
| active_window.bottom            | Gets bottom edge position     | 1040 (int)                                                    |
| active_win.topleft = (800, 400) | Sets window position          | None (modifies in place)                                      |
| active_win.isMaximized          | Checks if window is maximized | False (bool)                                               |
| active_win.isMinimized          | Checks if window is minimized | False (bool)                                               |
| active_win.isActive             | Checks if window is active    | True (bool)                                                |
| active_win.maximize()           | Maximizes the window          | None                                                          |
| active_win.restore()            | Restores from min/max         | None                                                          |
| active_win.minimize()           | Minimizes the window          | None                                                          |
| active_win.activate()           | Activates the window          | None                                                          |
| active_win.close()              | Closes the window             | None                                                          |


#### Be careful with `close()` method as it may bypass any save message dialogues



## Keyboard


### Key Names

- `PyAutoGUI` uses following `string names` to represent keyboard keys for functions like `press()`, `keyDown()`, and `hotkey()`. 
- Single characters work directly, while special keys use descriptive names.

| Key Name(s)                                                      | Description                |
| ---------------------------------------------------------------- | -------------------------- |
| 'a', 'b', 'c', 'A', 'B', 'C', '1', '2', '3', '!', '@', '#', etc. | Single character keys      |
| 'enter', 'return', '\\n'                                         | ENTER key                  |
| 'esc'                                                            | ESC key                    |
| 'shiftleft', 'shiftright'                                        | Left and right SHIFT keys  |
| 'altleft', 'altright'                                            | Left and right ALT keys    |
| 'ctrlleft', 'ctrlright'                                          | Left and right CTRL keys   |
| 'tab', '\\t'                                                     | TAB key                    |
| 'backspace', 'delete'                                            | BACKSPACE and DELETE keys  |
| 'pageup', 'pagedown'                                             | PAGE UP and PAGE DOWN keys |
| 'home', 'end'                                                    | HOME and END keys          |
| 'up', 'down', 'left', 'right'                                    | Arrow keys                 |
| 'f1', 'f2', 'f3', ..., 'f12'                                     | F1 to F12 keys             |
| 'volumemute', 'volumedown', 'volumeup'                           | Volume control keys        |
| 'pause'                                                          | PAUSE key                  |
| 'capslock', 'numlock', 'scrolllock'                              | Lock keys                  |
| 'insert'                                                         | INSERT key                 |
| 'printscreen'                                                    | PRINT SCREEN key           |
| 'winleft', 'winright'                                            | Windows keys (Windows)     |
| 'command'                                                        | COMMAND (⌘) key (macOS)    |
| 'option'                                                         | OPTION key (macOS)         |


```python
pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])
```

###  write()

- This function sends virtual key presses to the computer
- You want to set window as active before calling it
- function will enter the full string instantly, you can use optional argument to add a short pause between each character (`int/float` of seconds)
- It will automatically simulate holding down the `SHIFT` key

```python
pyautogui.click(100, 200); pyautogui.write('Hello, world!') # you can write on one line!

pyautogui.write('Hello, world!', 0.25) # this will write slowed down to quarter of a second between each letter
```

### keyDown(), keyUp() and press()

- `keyDown()` and `keyUp()` are **exactly the same** as `mouseDown()` and `mouseUp()` functions, they will send virtual key presses and releases to the computer
- `press()` function calls **both of these functions to simulate a complete key press**


example:
```python
# type a dollar sign ($) character (obtained by holding the SHIFT key and pressing 4)
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
```


### .hotkey()

- hotkey or shortcut is a combination of key presses to invoke some application function
- One of the most common ones are CTRL+C on windows, or CTRL+ALT+DEL etc

```python
#manual version
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

# Or just call hotkey function
pyautogui.hotkey('ctrl', 'c')
# CTRL-ALT-SHIFT-S
pyautogui.hotkey('ctrl', 'alt', 'shift', 's').
```