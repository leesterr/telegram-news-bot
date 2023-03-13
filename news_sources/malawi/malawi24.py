from bs4 import BeautifulSoup
import requests

source_url = 'https://malawi24.com/category/top-news/'


def malawi_news():
    source = requests.get(url=source_url)
    soup = BeautifulSoup(source.text, 'lxml')
    article = soup.find('article')
    headline = article.find('h3', class_='entry-title posts-list-title').text
    news_url = article.find('a', class_='excerpt-more')['href']
    main_content = requests.get(news_url)
    main_soup = BeautifulSoup(main_content.text, 'lxml')
    article = main_soup.find('article')
    news = article.find('div', class_='entry-content clearfix')
    dump = ''
    for line in news.find_all('p'):
        dump += line.text
    final = f'HEADLINE\n<b>{headline}</b>\n\n{dump}'
    return final

def malawi_news_short():
    source = requests.get(url=source_url)
    soup = BeautifulSoup(source.text, 'lxml')
    article = soup.find('article')
    headline = article.find('h3', class_='entry-title posts-list-title').text
    news_url = article.find('a', class_='excerpt-more')['href']
    final = f'HEADLINE\n<b>{headline}</b>\n\n{news_url}'
    return final
