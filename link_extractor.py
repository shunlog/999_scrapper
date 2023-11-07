#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests


def get_article_urls_from_category(category_page, page_num=1, max_page_num=2):
    '''Given a category page like this "https://999.md/ro/list/transport/cars",
    return the list of links in that category
    from the first page up until the last page, or until `max_page_num`, whichever is lower.

    Note: The boosted links are filtered out.
    '''
    def is_last_page(soup):
        paginator = soup.find("nav", "paginator")
        pages = paginator.find_all("li")
        curr_page = paginator.find("li", "current")
        return pages[-1] == curr_page

    def get_urls_from_page_soup(soup):
        def filter_boosted_links(ls):
            return [l for l in ls if 'booster' not in l]

        HOST = 'https://999.md'
        page_links = [a.get('href') for a in soup.table.find_all("a", "js-item-ad")]
        page_links = filter_boosted_links(page_links)
        return [HOST + ln for ln in page_links]

    def get_soup_for_current_page():
        payload = {'view_type': 'short', 'page_num': page_num}
        r = requests.get(category_page, params=payload)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        return soup

    if page_num > max_page_num:
        return []

    soup = get_soup_for_current_page()
    if is_last_page(soup):
        return []

    links = get_urls_from_page_soup(soup)
    return links + get_article_urls_from_category(category_page, page_num+1, max_page_num)

if __name__ == '__main__':
    category_page = "https://999.md/ro/list/transport/cars"
    articles = get_article_urls_from_category(category_page, max_page_num=2)
    print('\n'.join(articles))
