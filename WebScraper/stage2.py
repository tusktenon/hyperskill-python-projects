import requests
from bs4 import BeautifulSoup

url = input('Input the URL: ')
if not url.startswith('https://www.nature.com/articles/'):
    print('Invalid page!')
else:
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, 'html.parser')
    summary = {
        'title': soup.find('title').text,
        'description': soup.find('meta', {'name': 'description'}).get('content'),
    }
    print(summary)
