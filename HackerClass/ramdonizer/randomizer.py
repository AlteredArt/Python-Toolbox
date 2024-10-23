# WELCOME TO THE RANDOMIZER STUDY GUIDE
# COME BACK ONCE A DAY FOR A RANDOM SET OF TOPICS TO STUDY
import requests

params = {'userId': 1, 'id':2}
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, params)

if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(data)
else:
    print(f"Error: {response.status_code}")
