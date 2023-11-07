# 999 scrapper

The main functions:
- `get_article_urls_from_category` 
- `get_json_from_article_url`

`get_article_urls_from_category` is used in the following way:
``` sh
>>> category = "https://999.md/ro/list/transport/cars" 
>>> get_article_urls_from_category(category)
['https://999.md/ro/83893186', 'https://999.md/ro/84871503', 'https://999.md/ro/83602507', 'https://999.md/ro/84564679', 'https://999.md/ro/84464873', 'https://999.md/ro/81106087', 'https://999.md/ro/84871496', 'https://999.md/ro/84713023', 'https://999.md/ro/81866162', 'https://999.md/ro/84545477', 'https://999.md/ro/84158846', 'https://999.md/ro/84381141', 'https://999.md/ro/84781403', 'https://999.md/ro/82731994', 'https://999.md/ro/84508439', 'https://999.md/ro/81845397', 'https://999.md/ro/84614158', 'https://999.md/ro/81622028']

```


`get_json_from_article_url` is used in the following way:

``` sh
>>> url = 'https://999.md/ro/81845397'
>>> print(get_json_from_article_url(url))
```

``` json
{
    "article_name": "Apartament cu 2 camere, 65 m\u00b2, Botanica, Chi\u0219in\u0103u",
    "category": "Imobiliare",
    "subcategory": "Apartamente",
    "article_description": "Se vinde apartament cu 2 od\u0103i\n\u00cenc\u0103lzirea autonom\u0103\nBloc nou\nEste eliberat\nDisponibil in credit ipotecar",
    "properties": [
        {
            "name": "Suprafa\u021b\u0103 total\u0103",
            "value": "65   m\u00b2"
        },
        {
            "name": "Nivelul",
            "value": "10"
        },
        ...
        {
            "name": "Teren de joac\u0103"
        }
    ],
    "price": {
        "currency": "\u20ac",
        "price": "67900"
    },
    "converted_price": [
        {
            "currency": "$",
            "price": "71941"
        },
        {
            "currency": "lei",
            "price": "1307001"
        }
    ],
    "address": {
        "country": "Moldova",
        "locality": [
            "Chi\u0219in\u0103u mun.",
            "Chi\u0219in\u0103u",
            "Botanica",
            "str. Cetatea Alb\u0103",
            "143/1"
        ]
    },
    "phone_number": "+37369132328"
}
```

# RabbitMQ

The files `producer.py` and `consumer.py` use RabbitMQ to respectively queue and parse article url's,
and save them in files like this:`

``` sh
downloaded
├── 55283983.json
├── 71996588.json
├── 72034970.json
├── 75885230.json
├── 76960616.json
...
```
