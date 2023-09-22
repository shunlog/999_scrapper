#!/usr/bin/env python3
from bs4 import BeautifulSoup
from icecream import ic
from IPython import embed
import requests

HOST = 'https://999.md'

def get_articles_in_category(category_page, page=1, max_page=3):
    def is_last_page(soup):
        paginator = soup.find("nav", "paginator")
        pages = paginator.find_all("li")
        curr_page = paginator.find("li", "current")
        return pages[-1] == curr_page

    def get_article_links(soup):
        page_links = soup.table.find_all("a", "js-item-ad")
        return [HOST + a['href'] for a in page_links]

    def soup_page(page_num):
        payload = {'view_type': 'short', 'page': page_num}
        r = requests.get(category_page, params=payload)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        return soup

    if page >= max_page:
        return []

    soup = soup_page(page)
    if is_last_page(soup):
        return []

    articles = get_article_links(soup)
    return articles + get_articles_in_category(category_page, page+1, max_page)

category_page = HOST + "/ro/list/transport/cars"
articles = get_articles_in_category(category_page, 3, 5)
ic(articles)
