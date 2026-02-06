import requests
from decouple import config

URL = 'https://api.nasa.gov/planetary/apod'
API_KEY = config('API_KEY')


res = requests.get(URL, params={'api_key': API_KEY})
if not res.ok:
    exit(1)

print(res.json())