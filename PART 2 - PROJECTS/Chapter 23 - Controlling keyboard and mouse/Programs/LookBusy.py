""" 
Looking Busy
Many instant messaging programs determine whether you are idle, or away from your computer, by detecting a lack of mouse movement 
over some period of time—say, 10 minutes. 
Maybe you’re away from your computer but don’t want others to see your instant messenger status go into idle mode to give the impression that you’re slacking. 

Write a script to nudge your mouse cursor by one pixel to the left every 10 seconds, 
and then one pixel to the right 10 seconds after that. 

The nudge should be small and infrequent enough so that it won’t get in the way if you do happen to need to use your computer while the script is running.
"""
import pyautogui

pyautogui.PAUSE = 10 # pause EVERY call (module-level setting)

for i in range(30):
	pyautogui.move(- 1, 0) # move 1p to the left
	pyautogui.move(1,0) # move 1p to the right