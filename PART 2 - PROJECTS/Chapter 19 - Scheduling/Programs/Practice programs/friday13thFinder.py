# Find next 10 Friday the 13th dates
# Find previous 10 Friday 13th dates

import datetime as dt

# Function to find future dates
def findFutureFri13(start_date):
	print('Searching for the FUTURE dates...')
	fridays = [] # make a list of fridays
	current_day = start_date # start with current day
	one_day = dt.timedelta(days=1) # add one day to current day

	while len(fridays) < 10: # loop until you find 10 dates
		current_day += one_day # add one day to current day
		# fridays that are also 13th of the month
		if current_day.day == 13: # get the day nr and if it matches, continue
			if current_day.strftime('%A') == 'Friday': # get the day name
				fridays.append(current_day) # add it to the list if it's a match
				#print(f'Added {current_day} to the list')
	
	print(f'Future 10 Fridays the 13\'th are:')
	for friday in fridays:
		print(friday.strftime('%d %b %Y'))


# Function to find past dates
def findPastFri13(start_date):
	print('Searching for the PAST dates...')
	fridays = [] # make a list of fridays
	current_day = start_date # start with current day
	one_day = dt.timedelta(days=1) # add one day to current day

	while len(fridays) < 10: # loop until you find 10 dates
		current_day -= one_day # add one day to current day
		# fridays that are also 13th of the month
		if current_day.day == 13: # get the day nr and if it matches, continue
			if current_day.strftime('%A') == 'Friday': # get the day name
				fridays.append(current_day) # add it to the list if it's a match
				#print(f'Added {current_day} to the list')
	
	print(f'Past 10 Fridays the 13\'th are:')
	for friday in fridays:
		print(friday.strftime('%d %b %Y'))

# choose if you want to search back in time or in the future
choice = input(' Enter 1 to find NEXT 10 Friday the 13th dates \n Enter 2 to find PREVIOUS 10 Friday 13th dates \n >> ')
if choice == '1':
	now = dt.datetime.now()
	findFutureFri13(now)
elif choice == '2':
	now = dt.datetime.now()
	findPastFri13(now)
else: 
	print('Invalid input')