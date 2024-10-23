import requests

# Replace 'your_api_key' with your actual API key
api_key = 'your_api_key'
word = 'example'
url = f'https://api.dictionaryapi.dev/api/v2/entries/en/hello'

# headers = {
#     'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com',
#     'x-rapidapi-key': api_key
# }

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
