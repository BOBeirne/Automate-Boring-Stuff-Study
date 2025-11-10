# Example on how to use selenium attributes and methods
# Firefox changed to Chrome as I don't have FF installed.

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://autbor.com/example3.html')
elems = browser.find_elements(By.CSS_SELECTOR, 'p')

print(elems[0].text) # look at the first <p> element abd get its text
# This <p> tag puts content into a single paragraph.
print(elems[0].get_property('innerHTML')) # .text is the same as .get_property('innerHTML') but innerHTML is more specific to show the escape characters
# This <p> tag puts <b>content</b> into a <i>single</i> paragraph.
