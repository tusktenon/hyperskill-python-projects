import os
import string

import requests
from bs4 import BeautifulSoup

PAGE_DIR = 'Page_{page}'


def archive(pages, article_type):
    for page in range(1, pages + 1):
        print(f'Page {page}:')
        page_dir = PAGE_DIR.format(page=page)
        if not os.path.exists(page_dir):
            os.mkdir(page_dir)
        archive_page(page, article_type)


def archive_page(page, requested_type):
    response = requests.get(
        f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={page}'
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    for article in soup.find_all('article'):
        article_type = article.find('span', {'data-test': 'article.type'})
        if article_type.text == requested_type:
            link = article.find('a', {'data-track-action': 'view article'})
            save_article('https://www.nature.com' + link.get('href'), PAGE_DIR.format(page=page))


def save_article(url, save_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1').text.strip()
    teaser = soup.find('p', {'class': 'article__teaser'})
    filename = title.translate(str.maketrans(' ', '_', string.punctuation))
    filepath = os.path.join(save_dir, filename + '.txt')
    print(f'Saving "{title}"...')
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(teaser.text)


def main():
    pages = int(input('Number of pages: '))
    article_type = input('Article type: ')
    archive(pages, article_type)


if __name__ == '__main__':
    main()

