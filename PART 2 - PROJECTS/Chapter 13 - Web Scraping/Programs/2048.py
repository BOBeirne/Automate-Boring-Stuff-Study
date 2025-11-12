# This program goes to https://play2048.co/ and randomly uses 4 arrow keystrokes to play the game

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

Up =  Keys.ARROW_UP
Down = Keys.ARROW_DOWN
Left = Keys.ARROW_LEFT
Right = Keys.ARROW_RIGHT
key_choice = [Up, Down, Left, Right]


browser = webdriver.Chrome() # open a browser
browser.get('https://play2048.co/') # go to this link

browser.find_element(By.ID, 'ez-accept-necessary').click() # accept necessary cookies only

while True:
	for random.choice in key_choice: # pick a random key
		browser.find_element(By.TAG_NAME, 'html').send_keys(random.choice) # send the random key
		time.sleep(0.1) # wait 1/10th of a second to avoid getting blocked










