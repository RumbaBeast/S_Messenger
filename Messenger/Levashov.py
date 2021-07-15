#!/usr/bin/env python3
import time
from datetime import datetime

print('https://replit.com/@Levashov/messenger')

print(str(datetime.now()))

# 1 Database

db = [
    {
        'text': 'Hello',
        'name': 'Bran',
        'time': time.time()
    }
]


# 2 send message

def send_message(text, name):
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)


send_message('Как дела, Bran?', 'Николай')

send_message('Все круто, Колян!', 'Bran')


# 3 get messages

def get_messages(after):
    result = []

    for message in db:
        if message['time'] > after:
            result.append(message)

    return result


send_message('Where are you from?', 'Bran')

messages = get_messages(0)


# get_messages(db[-1]['time'])

def print_messages(base):
    for message in base:
        print(datetime.fromtimestamp(message['time']), message['name'])
        print(message['text'])
        print()
    print('-' * 25)


# print_messages(db)
send_message('Россия, брат!', 'Колян')

send_message('It is cool, bro!', 'Bran')
# print_messages(get_messages(messages[-1]['time']))

print_messages(get_messages(0))
