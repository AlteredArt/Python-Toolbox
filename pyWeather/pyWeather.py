import requests

city_name = 'Colorado Springs'
API_Key = 'b6a61e5b7a18005040feaa658d3a6eed'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=imperial'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # print(data['weather'])
    print(data['weather'][0])
    print('Weather is',data['weather'][0]['description'])
    print('Current Temperature',data['main']['temp'])
    print('Current Temperature feels like',data['main']['feels_like'])
    print('Humidity is',data['main']['humidity'])




else:
    print('not connected')