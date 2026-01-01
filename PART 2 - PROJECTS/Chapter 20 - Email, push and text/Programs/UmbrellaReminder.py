# using data from https://weather.gov/ scrape weather data and send a notification if the weather in chosen location will be rainy that day
# Location New york - https://forecast.weather.gov/MapClick.php?lat=40.7130466&lon=-74.0072301 (New York City, Central Park (KNYC))
#<p class="myforecast-current"> Light Snow</p>
#<div class="col-sm-10 forecast-text">Mostly cloudy through mid morning, then becoming sunny, with a steady temperature around 27. Wind chill values between 10 and 15. Blustery, with a northwest wind 18 to 23 mph, with gusts as high as 33 mph. </div>
# Babalablabs-testing
"""
1. Download the webpage using requests
2. Parse the HTML with BeautifulSoup
3. Find the element(s) that contain the weather forecast text
4. Check if "rain" appears in that text
5. Print result or take action
"""

import requests, bs4

reqInfo = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.7130466&lon=-74.0072301') # Link for weather in New York City, Central Park (KNYC)
reqStatus = reqInfo.raise_for_status()
#print(f'Request status: {reqStatus}') # check for errors
#if reqStatus == None:
	#print('Successfully retrieved webpage.')

soup = bs4.BeautifulSoup(reqInfo.text, 'html.parser') # create bs object
#print(soup.prettify()) # print out full html code
currentForecastTag = soup.select('p.myforecast-current') # find <p class="myforecast-current"> tag
todayForecastTag = soup.select('div.col-sm-10.forecast-text') 
#print(currentForecastTag)
#print(todayForecastTag)
# [<p class="myforecast-current">A Few Clouds</p>]
currentWeather = currentForecastTag[0].get_text() # get the actual status
print(f'Current weather: {currentWeather}') 
todayForecastWeather = todayForecastTag[0].get_text() # get weather prediction text
print(f'Today\'s Forecast: {todayForecastWeather}')

flag = False
keywords = ['rain', 'rainy', 'drizzle', 'storm', 'rainstorm', 'shower', 'snow', 'snowfall', 'snowstorm', 'mist', 'sprinkle', 'raindrops'] # there are too many ways to say "rain"
for word in keywords:
	if word in currentWeather.lower():
		print('I\'s raining now, bring an umbrella.')
		requests.post('https://ntfy.sh/Babalablabs-testing', 'I\'s raining now, bring an umbrella!')
		flag = True
	elif word in todayForecastWeather.lower():
		print('It will rain today, bring an umbrella.')
		requests.post('https://ntfy.sh/Babalablabs-testing', 'It will rain later today, bring an umbrella!')
		flag = True
	else:
		pass

if flag == False:
	print('No rain expected today.')
