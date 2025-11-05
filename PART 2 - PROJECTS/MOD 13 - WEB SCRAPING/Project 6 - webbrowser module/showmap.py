# Launches a map in the browser using an address from the cli or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1: # check if cli arg has been provided
	address = ' '.join(sys.argv[1:]) # get address from cli

else:
	address = pyperclip.paste() # get address from clipboard

webbrowser.open('https://www.openstreetmap.org/search?query=' + address)
