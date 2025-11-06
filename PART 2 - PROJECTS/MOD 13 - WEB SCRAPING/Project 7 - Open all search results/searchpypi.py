# Open all search results from pypi.org with one click
# search page - https://pypi.org/search/?q=%3CSEARCH_TERM_HERE%3E

import requests, sys, webbrowser, bs4

print('Searching...') # display text while downloading the results page
res = requests.get('https://pypi.org/search/?q=' + ''.join(sys.argv[1:])) # get the search page matching the search term from the command line
res.raise_for_status() # check for any issues downloading
print('Search complete.') # let me know the search is complete

soup = bs4.BeautifulSoup(res.text, 'html.parser') # create a BeautifulSoup object with the search results page as a string
link_elems = soup.select('.package-snippet__name') # find all <a> elements with class="package-snippet__name", this is a pattern that all search result pages have in common *
num_open = min(5, len(link_elems)) # limit the number of results to open to 5 or less depending on the number of results
print('Opening', num_open, 'search results...') # let me know how many results will be opened

for i in range(num_open):
	url_to_open = 'https://pypi.org' + str(link_elems[i].get('href')) # get the href attribute of the <a> element **
	print('Opening', url_to_open) 
	webbrowser.open(url_to_open) # open the URL in a new tab

# * while working through this book the package_snippet has been changed to package-snippet__name, in order for code to run needs to be updated
# ** this line of code in the book has an error, it requires a str() to convert literals to strings, 
#  otherwise it will return error: "Operator "+" not supported for types "Literal['https://pypi.org']" and "_AttributeValue | None""