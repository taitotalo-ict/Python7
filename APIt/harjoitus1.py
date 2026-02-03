import requests
from pprint import pprint


base_url = 'https://api.tvmaze.com'
res = requests.get(url=base_url+'/search/shows', params={'q': 'putous'})
if not res.ok:
    exit(1)

data = res.json()
# pprint(len(data))
# pprint(data[0])
show_id = data[0]['show']['id']

res = requests.get(url=base_url+f'/shows/{show_id}/episodes')
if not res.ok:
    exit(1)

data = res.json()
# pprint(len(data))
for episode in data:
    season = episode['season']
    number = episode['number']
    airdate = episode['airdate']
    print(f'Season: {season} - Episode {number} - {airdate}')
