# Downloads 10 XKCD comics

import requests, os, time, bs4

url = 'https://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in cwd ./xkcd, check if folder already exists and if it does just continue instead of throwing an error

num_downloads = 0
max_downloads = 10 # limit nr of downloaded comics to 10

while not url.endswith('#') and num_downloads < max_downloads: # loop as long as not at the end of the comic and number of downloads is under the limit
	print(f'Downloading the page {url}...')
	res = requests.get(url) # download page
	res.raise_for_status() # check for any issues downloading
	soup = bs4.BeautifulSoup(res.text, 'html.parser') # create a BeautifulSoup object with the search results page as a string
	# find the url of the comic image
	comic_elem = soup.select('#comic img') # find all <img> elements with id="comic"
	if comic_elem == []: # if there is no comic image
		print('Could not find comic image.')
	else:
		comic_url = 'https:' + str(comic_elem[0].get('src')) # get the src attribute of the <img> element
		print(f'Downloading image {comic_url}...') # 
		res = requests.get(comic_url) # download the image
		res.raise_for_status() # check for any issues downloading
		
		# save the image to ./xkcd
		image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') # open file for writing in binary mode
		for chunk in res.iter_content(100000): # save the file in chunks of 100000 bytes
			image_file.write(chunk) # write each chunk to the file
		image_file.close() # close the file after each chunk to free up memory and avoid errors 
		
	# get the previous button's url
	prev_link = soup.select('a[rel="prev"]')[0] # find all <a> elements with rel="prev"
	url = 'https://xkcd.com' + str(prev_link.get('href'))
	num_downloads += 1
	time.sleep(1) # wait 1 second before downloading the next page to avoid getting blocked by the website for too many requests per minute

print('Done.')