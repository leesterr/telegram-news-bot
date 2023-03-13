import requests
from bs4 import BeautifulSoup

source_url = 'https://durovscode.com/tag/news'


def durov_source():
    source = requests.get(url=source_url)
    soup = BeautifulSoup(source.text, 'lxml')
    article = soup.find('article', class_='NewsCard_card__L0I13')
    url = article.find('a', class_='NewsCard_link__qIUwP')['href']
    full_url = f'https://durovscode.com{url}'
    headline = article.text
    news_details = requests.get(full_url)
    soup_news_details = BeautifulSoup(news_details.text, 'lxml')
    news = soup_news_details.find('div', class_='NewsDetail_content__vm5jG').text
    final_news = f'HEADLINE\n<b>{headline}</b>\n\n{news}'
    return final_news
