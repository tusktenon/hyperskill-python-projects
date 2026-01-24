import string

import requests
from bs4 import BeautifulSoup

URL = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

for article in soup.find_all('article'):
    article_type = article.find('span', {'data-test': 'article.type'})
    if article_type.text == 'News':
        link = article.find('a', {'data-track-action': 'view article'})
        link_response = requests.get('https://www.nature.com' + link.get('href'))
        link_soup = BeautifulSoup(link_response.content, 'html.parser')
        title = link_soup.find('h1').text.strip()
        filename = title.translate(str.maketrans(' ', '_', string.punctuation))
        teaser = link_soup.find('p', {'class': 'article__teaser'})
        print(f'Saving "{title}"...')
        with open(filename + '.txt', 'w', encoding='utf-8') as file:
            file.write(teaser.text)
