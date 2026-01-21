""" 
While you can send keystrokes to an application’s text fields with pyautogui.write(), you can’t use PyAutoGUI alone to read the text already inside a text field. 
This is where the pyperclip module can help. You can use PyAutoGUI to obtain the window for a text editor such as Mu or Notepad, 
bring it to the front of the screen by clicking it, click inside the text field, 
and then send the CTRL-A or -A hotkey to “select all” and CTRL-C or -C hotkey to “copy to clipboard.” 
Your Python script can then read the clipboard text by running import pyperclip and pyperclip.paste().

Write a program that follows this procedure for copying the text from a window’s text fields. 
Use pyautogui.getWindowsWithTitle('Notepad') (or whichever text editor you choose) to obtain a Window object. 
The top and left attributes of this Window object can tell you where this window is, while the activate() method will ensure that it is at the front of the screen. 
You can then click the main text field of the text editor by adding, say, 100 or 200 pixels to the top and left attribute values with pyautogui.click() to put the keyboard focus there. 
Call pyautogui.hotkey('ctrl', 'a') and pyautogui.hotkey('ctrl', 'c') to select all the text and copy it to the clipboard. Finally, 
call pyperclip.paste() to retrieve the text from the clipboard and paste it into your Python program. 
From there, you can use this string however you want, but just pass it to print() for now.

Note that the window functions of PyAutoGUI only work on Windows as of PyAutoGUI version 1.0.0, and not on macOS or Linux.
"""

import pyautogui as gui
import pyperclip as clip

# find window by title like notepad
window_obj = gui.getWindowsWithTitle('Notepad') # get window object
print(window_obj)
window_obj[0].activate() # activate the notepad window

gui.moveTo(300, 300) # move to selected coordinate
gui.hotkey('ctrl', 'a') # select all txt
copy = gui.hotkey('ctrl', 'c') # copy into clipboard
window_txt = clip.paste() # paste extracted str into variable
print(window_txt) # print the string
