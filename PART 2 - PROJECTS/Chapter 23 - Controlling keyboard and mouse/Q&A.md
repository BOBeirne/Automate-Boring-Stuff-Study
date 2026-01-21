# Practice Questions

## 1  How can you trigger PyAutoGUI’s fail-safe to stop a program?

Quickly move the cursor to one of the corners of the screen

## 2  What function returns the current screen resolution?

`pyautogui.size()` 

## 3  What function returns the coordinates for the mouse cursor’s current position?

`pyautogui.position()`

## 4  What is the difference between pyautogui.moveTo() and pyautogui.move()?

`pyautogui.moveTo()` moves the cursor to specific coordinates, meanwhile `pyautogui.move()` moves the cursor x/y pixels relative to it's current position

## 5  What functions can be used to drag the mouse?

`pyautogui.drag()` and `.dragTo()`

## 6  What function call will type out the characters of "Hello, world!"?

`pyautogui.write('Hello, world!')` but you may first want to make sure the window is active

## 7  How can you do key presses for special keys, such as the keyboard’s left arrow key?

`pyautogui.press('left')`

## 8  How can you save the current contents of the screen to an image file named screenshot.png?

```python
img = pyautogui.screenshot() # get pillow object
img.save('screenshot.png') # save into the file
```
there is also one-liner option: `pyautogui.screenshot('screenshot.png')`

## 9  What code would set a two-second pause after every PyAutoGUI function call?

`pyautogui.PAUSE = 2`

## 10  If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?

Selenium is best, it interacts via elements so the window size or position does not matter
PyAutoGUI should be last resort

## 11  What makes PyAutoGUI error prone?

If a window is in the wrong place on a desktop or some pop-up appears unexpectedly, your script could be clicking the wrong things on the screen
Also if you are using function `locateOnScreen()` and image source is blurry or is not beferctly, axactly like the window you are looking for it will not find it unless you use confidence score, which requires another library `opencv` to be installed

## 12  How can you find the size of every window on the screen that includes the word Notepad in its title?

```python
import pyautogui
for window in pyautogui.getWindowsWithTitle('Notepad'):
	print(window.width, window.height)
```

## 13  How can you make, say, the Firefox browser active and in front of every other window on the screen?

```python
ff_list = pyautogui.getWindowsWithTitle('Firefox') # get the ff window objects list
ff_list[0].activate() # activate the 1st window match
```