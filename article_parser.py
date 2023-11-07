#!/usr/bin/env python3
from collections import OrderedDict
import json
import requests
from bs4 import BeautifulSoup

HOST = 'https://999.md'

def get_soup_from_url(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_info_from_article_soup(soup) -> dict:
    '''For the soup of an article url like "https://999.md/ro/73960104",
    return a dictionary with all the relevant information found on the page.
    '''

    info = OrderedDict()
    info['article_name'] = soup.find("h1", attrs={'itemprop': "name"}).get_text(strip=True)

    breadcrumbs = [li.get_text(strip=True) for li in soup.find("div", "breadcrumbs").find_all("li")]
    info['category'] = breadcrumbs[-3]

    info['subcategory'] = breadcrumbs[-2]

    desc_div = soup.find("div", attrs={'itemprop': "description"})
    info['article_description'] = desc_div.get_text(strip=True) if desc_div else None

    properties_dict = []
    props_ls = soup.find_all("li", itemprop="additionalProperty")
    for li in props_ls:
        prop = {}
        prop['name'] = li.find(itemprop='name').get_text(strip=True)

        value_elem = li.find(itemprop='value')
        if value_elem:
            prop['value'] = value_elem.get_text(strip=True)

        if li.find('a'):
            prop['category_url'] = HOST + li.find('a')['href']
        properties_dict.append(prop)
    info['properties'] = properties_dict

    prices = []
    for p, c in zip(soup.find_all("span", itemprop="price")[:3], soup.find_all("span", itemprop='priceCurrency')[:3]):
        prices.append({'currency': c['content'],
                       'price': p['content']})
    if prices:
        info['price'] = prices[0]
        info['converted_price'] = prices[1:]
    else:
        info['price'] = None

    info['address'] = {'country': soup.find(itemprop='addressCountry')['content'],
                       'locality': [i['content'] for i in soup.find_all(itemprop='addressLocality')]}

    phone_number = soup.find(lambda e: e.has_attr('href') and e['href'][:4] == "tel:")
    if phone_number:
        info['phone_number'] = phone_number['href'][4:]

    return info

def get_json_from_article_url(url):
    soup = get_soup_from_url(url)
    info_dict = get_info_from_article_soup(soup)
    return json.dumps(info_dict, indent=4)

if __name__ == '__main__':
    url = "https://999.md/ro/83797072"
    print(get_json_from_article_url(url))
