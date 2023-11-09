#!/usr/bin/env python3
import os
import sys
import threading
import pika
from article_parser import get_json_from_article_url

QUEUE = '999'

def callback(ch, method, properties, body):
    url = body.decode()
    DIR = "./downloaded"

    print(f" [x] Received {url}")

    article_id = url[url.rfind('/')+1:]
    path = f'{DIR}/{article_id}.json'

    if os.path.isfile(path) and os.path.getsize(path) > 0:
        print(f" [.] Url is already parsed: {path}")
    else:
        with open(path, 'w') as f:
            f.write(get_json_from_article_url(url))
        print(f" [+] Parsed url: {path}")

    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(" [x] Done")


def start_consuming():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE, durable=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE, on_message_callback=callback)

    channel.start_consuming()


if __name__ == '__main__':

    n_threads = int(sys.argv[1]) or 1

    for _ in range(n_threads):
        threading.Thread(target=start_consuming).start()
