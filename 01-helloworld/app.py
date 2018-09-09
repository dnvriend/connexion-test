#!/usr/bin/env python3
import connexion
import logging

def get_messages(n: int = 10):
    return [f'Hello World {x}!' for x in range(1, n)]

def get_messages_root():
    return get_messages(25)

def get_message():
    return "Hello World!"

logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080, server='gevent')