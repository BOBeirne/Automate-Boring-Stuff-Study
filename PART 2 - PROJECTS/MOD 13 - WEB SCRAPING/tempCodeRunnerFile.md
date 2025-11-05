import requests
city_name = 'San Francisco'
state_code = 'CA'
country_code = 'US'
API_key = '8d228cc79e2246643999faefa226726e' # Put your API here
response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')

print(response.text) # returns Python string

import json
response_data = json.loads(response.text)
print(response_data) # Returns Python data structure