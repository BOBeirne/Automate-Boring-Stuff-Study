"""
Some websites allow you to view their text contents but make it difficult to save or even copy and paste the text to your computer. 
You may see them as PDFs embedded within the web page

The PyAutoGUI library covered in Chapter 23 can take screenshots and save them to an image, 
while the Pillow library covered in Chapter 21 can crop images. 
PyAutoGUI also has a MouseInfo application for finding XY coordinates on the screen.

Write a program named ocrscreen.py that takes a screenshot, 
crops the image to just the text portion in the screenshot, 
then passes it on to PyTesseract for OCR. 
The program should append the recognized text to the end of a text file named output.txt. 

Here is a template for the ocrscreen.py program:

import pyautogui
# TODO - Add the additionally needed import statements.

# The coordinates for the text portion. Change as needed:
LEFT = 400
TOP = 200
RIGHT = 1000
BOTTOM = 800

# Capture a screenshot:
img = pyautogui.screenshot()

# Crop the screenshot to the text portion:
img = img.crop((LEFT, TOP, RIGHT, BOTTOM))

# Run OCR on the cropped image:
# TODO - Add the PyTesseract code here.

# Add the OCR text to the end of output.txt:
# TODO - Call open() in append mode and append the OCR text.

This program should let you scroll the embedded, unsavable text into view in your browser, 
run the program, and then scroll the PDF to the next page of content. 
Once done, you’ll have your own copy of the document’s text. 
(If you read Chapter 23, you’ll also learn how you can make your script simulate key presses to scroll the web page for you.)
"""


import pyautogui as gui
import pytesseract as tess
from PIL import Image as img
import time

time.sleep(5) #pause for 5 seconds to have time for window selection

# The coordinates for the text portion. Change as needed:
LEFT = 270
TOP = 100
RIGHT = 1200
BOTTOM = 1000

# Capture a screenshot
image = gui.screenshot(region=(LEFT,TOP,RIGHT,BOTTOM))

# Run OCR on the cropped image:
text = tess.image_to_string(image)
print(text)

# Add the OCR text to the end of output.txt:
with open('output.txt', 'a') as f: # append
	f.write(text)