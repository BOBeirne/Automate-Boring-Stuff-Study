from playwright.sync_api import sync_playwright
playwright = sync_playwright().start() # start playwright
browser = playwright.chromium.launch(headless=False, slow_mo=500) # open browser in NON-headless mode
page = browser.new_page() # open new page
page.goto('https://autbor.com/example3.html') # go to the specified link
# <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>

page.locator('html').press('End') # move the cursor to the end of the page
page.locator('html').press('Home') # move the cursor to the beginning of the page

browser.close() # close the browser
playwright.stop() # stop playwright