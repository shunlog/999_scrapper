# 999 scrapper

`example_links.txt` contains a sample output of the following:
``` sh
./in_class.py > example_links.txt
```


`homework.py` outputs a JSON like this (for example for [this article](https://999.md/ro/83797072)):

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
        {
            "name": "Num\u0103r de nivele",
            "value": "11"
        },
        {
            "name": "Num\u0103rul de camere",
            "value": "Apartament cu 2 camere"
        },
        {
            "name": "Autorul anun\u021bului",
            "value": "Agen\u021bie"
        },
        {
            "name": "Fond locativ",
            "value": "Construc\u0163ii noi"
        },
        {
            "name": "Gata de intrare"
        },
        {
            "name": "Mobilat"
        },
        {
            "name": "Tehnic\u0103 de uz casnic"
        },
        {
            "name": "\u00cenc\u0103lzire autonom\u0103"
        },
        {
            "name": "Aparat de aer condi\u021bionat"
        },
        {
            "name": "Geamuri termopan"
        },
        {
            "name": "Parchet"
        },
        {
            "name": "U\u0219\u0103 blindat\u0103"
        },
        {
            "name": "Linie telefonic\u0103"
        },
        {
            "name": "Interfon"
        },
        {
            "name": "Internet"
        },
        {
            "name": "Cablu TV"
        },
        {
            "name": "Ascensor"
        },
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
