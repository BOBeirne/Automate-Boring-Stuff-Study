from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://autbor.com/example3.html')

link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
print(type(link_elem))
# <class 'selenium.webdriver.remote.webelement.WebElement'>
link_elem.click() # follows the 'This text is a link' link and clicks on it