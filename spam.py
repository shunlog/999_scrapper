#!/usr/bin/env python3
import requests
import time


i = 20
while True:
    i += 1
    print("Iteration", i)
    url = "https://999.md/ro/73960104"

    headers = {
        'User-Agent': 'BMW 66665 {}.0'.format(i),
    }
    time.sleep(2)

    r = requests.get(url, headers=headers)
    print(r)


# html = r.text
# soup = BeautifulSoup(html, 'lxml')
