import requests
from decouple import config
from pprint import pprint
from pathlib import Path


URL = 'https://api.nasa.gov/planetary/apod'
API_KEY = config('API_KEY')
BASEDIR = Path(__file__).parent

res = requests.get(URL, params={'api_key': API_KEY, 'count': 10})
if not res.ok:
    exit(1)

# pprint(res.json())
for image_data in res.json():
    if image_data['media_type'] != 'image':
        print('Media ei ole kuva. Jatketaan seuraavalle.')
        continue
    
    year, month, _ = image_data['date'].split('-')
    image_folder = BASEDIR / 'images' / year / month
    # if not image_folder.exists():
    image_folder.mkdir(parents=True, exist_ok=True)

    image_url = image_data['url']
    filename = image_url.split('/')[-1] # Oletetaan, ettei ole query parametria
    image_path = image_folder / filename
    if image_path.exists():
        print('Kuva on jo ladattu. Ohitetaan sen.')
        continue

    res = requests.get(image_url)
    if not res.ok:
        print('Kuva ei voitu ladata. Ohitetaan.')
        continue
    with open(image_path, 'wb') as file:
        file.write(res.content)

    # text_path = image_folder / (image_path.stem + '.txt')
    text_path = image_path.with_suffix('.txt')
    with open(text_path, 'w') as file:
        file.write(f'Title: {image_data['title']}\n')
        file.write(f'Date: {image_data['date']}\n')
        file.write(f'Explanation: {image_data['explanation']}\n')
    
#     text_path.write_text(f'''
# Title: {image_data['title']}
# Date: {image_data['date']}
# Explanation: {image_data['explanation']}
# ''')
    
#     text_path.write_text(
#         f'Title: {image_data['title']}\n' +
#         f'Date: {image_data['date']}\n' +
#         f'Explanation {image_data['explanation']}\n'
#     )