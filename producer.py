#!/usr/bin/env python3
import pika
import sys
from link_extractor import get_article_urls_from_category

QUEUE = '999'

def publish(channel, message):
    channel.basic_publish(
        exchange='',
        routing_key='999',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    print(f" [x] Sent {message}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE, durable=True)

category = "https://999.md/ro/list/transport/cars"
for url in get_article_urls_from_category(category):
    publish(channel, url)

connection.close()
