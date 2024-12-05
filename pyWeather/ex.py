# import requests


# city_name = 'Colorado Springs'
# API_Key = 'b6a61e5b7a18005040feaa658d3a6eed'

# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=imperial'

# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     # print(data['weather'])
#     print(data['weather'][0])
#     print('Weather is',data['weather'][0]['description'])
#     print('Current Temperature',data['main']['temp'])
#     print('Current Temperature feels like',data['main']['feels_like'])
#     print('Humidity is',data['main']['humidity'])
# else:
#     print('not connected')

import requests
from datetime import datetime, timedelta

# Replace with your own OpenWeather API key
API_KEY = 'b6a61e5b7a18005040feaa658d3a6eed'

# Function to get historical weather data for a city
def get_historical_weather(city_name, date):
    # Get latitude and longitude for the city
    geocode_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    response = requests.get(geocode_url)
    if response.status_code != 200:
        print("Failed to get city coordinates")
        return None
    
    data = response.json()
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    
    # Convert date to Unix timestamp for the historical query
    date_unix = int(date.timestamp())
    
    # Make request to get historical weather data (using One Call API)
    historical_url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={date_unix}&appid={API_KEY}"
    historical_response = requests.get(historical_url)
    if historical_response.status_code != 200:
        print("Failed to get historical data")
        return None
    
    historical_data = historical_response.json()
    
    # Extract temperature data and find the minimum temperature
    temperatures = [hour['temp'] for hour in historical_data['hourly']]
    min_temp = min(temperatures)
    
    return min_temp

# Example usage
city = 'London'
date = datetime.now() - timedelta(days=30)  # Set to 30 days ago or any other desired date
min_temp = get_historical_weather(city, date)

if min_temp is not None:
    print(f"The historical low temperature in {city} on {date.strftime('%Y-%m-%d')} was {min_temp - 273.15:.2f}°C")
