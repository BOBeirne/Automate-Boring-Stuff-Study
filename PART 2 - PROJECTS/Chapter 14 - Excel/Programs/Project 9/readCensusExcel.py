# script that can read from the census spreadsheet file and calculate statistics for each county in a matter of seconds.

import openpyxl, pprint

print('Opening the workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx') # load workbook object
sheet = wb['Population by Census Tract'] # work on specific sheet
county_data = {} # initialise empty dictionary
"""
dictionary's keys structure:
county_data[state abbrev][county]['tracts']
county_data[state abbrev][county]['pop']
"""

# TODO Fill in country_data with each county's population and tracts

print('Reading rows...')
for row in range(2, sheet.max_row + 1): # iterate through each row except the header row
	# each row in the spreadsheet has data for one census tract
	state = sheet['B' + str(row)].value # get the state name
	county = sheet['C' + str(row)].value # get the county name
	pop = sheet['D' + str(row)].value # get the population

	# make sure the key for particular stat exists, cannot add data to it without initializing a key
	county_data.setdefault(state, {}) # create state key with empty dictionary

	# make sure key for this specific county in this specific state exists, cannot add data to it without initializing a key
	county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})
	# Since setdefault() will do nothing if the key already exists, you can call it on every iteration of the for loop without a problem.

	# Each row represents on census tract, increment by one each iteration of the loop
	county_data[state][county]['tracts'] += 1

	# increase the county pop by the pop in this census tract on each iteration of the loop
	county_data[state][county]['pop'] += int(pop)

# After the for loop has finished, the county_data dictionary should contain all of the population and tract information keyed by county and state.
	# TODO open new txt file and write contents to it

print('Writing results...')
result_file = open('census2010.py', 'w') # open file for writing
result_file.write('allData = ' + pprint.pformat(county_data)) # write data to the file as a one line string formatted as valid Python code. Thanks to that you can import it like a module
result_file.close() # close file
print('Done.')