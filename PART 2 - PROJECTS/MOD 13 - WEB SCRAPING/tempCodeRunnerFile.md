from selenium import webdriver
browser = webdriver.Chrome()
type(browser) # <class 'selenium.webdriver.chrome.webdriver.WebDriver'>
browser.get('https://inventwithpython.com/') # open a page in the browser