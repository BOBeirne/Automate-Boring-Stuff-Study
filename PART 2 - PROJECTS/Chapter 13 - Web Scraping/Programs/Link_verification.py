# This program if given a link will test all <a> links on the webpage to test if it results in 404 error. It will print out any broken links.
# tested on : https://github.com/BOBeirne with result: Link verification complete, total of 106 links checked, 55 404 errors found.

import requests, time
from playwright.sync_api import sync_playwright

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' } # had to be included as many websites block my IP if not included

browser = sync_playwright().start() # start playwright
browser = browser.chromium.launch(headless=False, slow_mo=500) # open browser in NON-headless mode
page = browser.new_page() # open new page
base_link = input('Enter a link: ')
page.goto(base_link) # go to provided link
links = page.query_selector_all('a') # find all <a> tags

# initialise counters
link_counter = 0
error_404 = 0
error_403 = 0


for link_element in links:
	link_counter += 1
	href = link_element.get_attribute('href')
	print('Checking link:', href)
	if href:
		if href.startswith(('#', 'mailto:', 'tel:','javascript:')):
			print('Skipping non-HTTP link') # Skip non-HTTP schemes
			continue
		if not href.startswith(('http', 'https')): # if NOT a base, full URL
			base_clean_url = base_link.strip('/') # remove any extra trailing slashes from the base link
			if not href.startswith('/'): # if NOT a relative URL
				href = '/' + href # add a leading slash to the
			full_url = base_clean_url + href # combine the base URL with the relative URL
		else:
			full_url = href # it's already an absolute url
		
		time.sleep(1) # wait 1 second before downloading the next page to avoid getting blocked by the website for too many requests per minute

	try:
		response = requests.get(full_url, timeout=5) # send a GET request to the link
		if response.status_code == 404: # if the response status code is 404
			print(f'Broken link with 404 error: {full_url}')
			error_404 += 1 
		#if response.status_code == 403:
			#print(f'Broken link with 403 error, Forbidden.: {full_url}') 
			#error_403 += 1 # many links return this error so it's a good way to use this loop to see if it catches specified errors
		#elif response.status_code >= 400:
			#print(f'Broken link with error {response.status_code}: {full_url}') # raise an exception if the request was not successful for any other error
	except requests.exceptions.RequestException as error_msg:
		print(f'Error downloading  {error_msg}')

browser.close() # close the browser
print(f'Link verification complete, total of {link_counter} links checked, {error_404} 404 errors found.')

