import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.python.org/')
if not res.ok:
    exit(1)

soup = BeautifulSoup(res.text, 'html.parser')

version = soup.find(class_='small-widget download-widget').find('a').text.split(' ')[1]
print(version)


# p_elems = soup.find_all('p')
# for p_elem in p_elems:
#     text = p_elem.get_text(strip=True)
#     if text.startswith('Latest'):
#         print(text.split(' ')[1])
