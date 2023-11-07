#!/usr/bin/env python3
import article_parser
import link_extractor

articles = link_extractor.get_article_urls_from_category("https://999.md/ru/list/real-estate/apartments-and-rooms?o_30_241=894&applied=1&eo=12900&eo=12912&eo=12885&eo=13859&ef=32&ef=33&o_33_1=776", max_page_num=2)
for url in articles:
    print(url)
    print(article_parser.get_json_from_article_url(url))
