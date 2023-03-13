import requests
from bs4 import BeautifulSoup

source_url = 'https://www.bbc.com/news'


def bbc_world():
    try:
        source_news = requests.get(source_url)
        soup = BeautifulSoup(source_news.text, 'lxml')
        main = soup.find('div', class_='gs-c-promo-body gs-u-display-none@m gs-u-display-inline-block '
                                       'gs-u-mt@xs gs-u-mt0@m gel-1/3@m')

        headline = main.find('a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link '
                                         'gel-paragon-bold nw-o-link-split__anchor')
        href = headline['href']

        summary = main.find('p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary')
        full_href = f'https://www.bbc.com{href}'

        final_article = f'HEADLINE\n<b>{headline.text}</b>\n\n{summary.text}\n{full_href}'
        return final_article
    except AttributeError:
        return '<b>An error occurred</b>'

