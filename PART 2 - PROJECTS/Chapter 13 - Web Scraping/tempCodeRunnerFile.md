from playwright.sync_api import sync_playwright
playwright = sync_playwright().start() # start playwright
browser = playwright.chromium.launch(headless=False, slow_mo=500) # open browser in NON-headless mode
page = browser.new_page() # open new page
page.goto('https://autbor.com/example3.html') # go to the specified link
# <Response url='https://autbor.com/example3.html' request=<Request url='https://autbor.com/example3.html' method='GET'>>
page.click('input[type="checkbox"]') # check the checkbox
page.click('input[type="checkbox"]') # uncheck the checkbox
page.click('a') # click the link
page.go_back() # go back to the previous page

checkbox_elem = page.get_by_role('checkbox') # get the checkbox element using Locator method
checkbox_elem.check() # check the checkbox
checkbox_elem.uncheck() # uncheck the checkbox

checkbox_elem.set_checked(True) # check the checkbox
checkbox_elem.set_checked(False) # uncheck the checkbox

page.get_by_text('is a link').click() # click the link with text "is a link"

browser.close() # close the browser
playwright.stop() # stop playwright