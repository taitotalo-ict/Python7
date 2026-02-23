import requests
from bs4 import BeautifulSoup

res = requests.get('https://realpython.github.io/fake-jobs/')
if not res.ok:
    exit(1)

soup = BeautifulSoup(res.text, 'html.parser')

# jobs_container = soup.find(id='ResultsContainer')
# for job_card in jobs_container.children:
#     print(job_card)

job_count = 0
jobs = soup.find_all(class_='card-content')
for job_card in jobs:
    location = job_card.find('p', class_='location').string.strip() # type: ignore
    # state = location.split(',')[1].strip()
    if not location.endswith('AE'):
        continue
    
    title = job_card.find('h2', class_='title').string  #type: ignore
    link = job_card.find('a', string='Apply')['href']   #type: ignore
    
    print(f'Title: {title}')
    print(f'Location: {location}')
    print(f'Application link: {link}\n')

    job_count += 1

print(f'Total jobs offer: {job_count}')
