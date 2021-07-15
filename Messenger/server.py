import time
from datetime import datetime
from translate import Translator
from pyjokes import get_joke
from flask import Flask, request
from werkzeug.exceptions import abort

app = Flask(__name__)

db = [
    {
        'text': 'Hello',
        'name': 'Bran',
        'time': 0.1
    }
]


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    count_messages = 0
    users = 0
    name = ""
    for message in db:
        count_messages += 1
        if message['name'] != name:
            users += 1
        name = message['name']
    return {
        # 'time0':    str(datetime.now()),
        'name': "WhiteSheep",
        'status': True,
        'count': count_messages,
        # 'MESSAGES': len(db),
        'users': users,
        'time': datetime.now().strftime('%H:%M:%S'),
    }


@app.route("/send", methods=['POST'])
def send_message():
    data = request.json
    # check data is dict with text & name
    if not isinstance(data, dict):
        return abort(400)
    if 'text' not in data or 'name' not in data:
        return abort(400)

    text = data['text'].strip()
    name = data['name'].strip()

    # check text & name are valid strings
    if not isinstance(text, str) or not isinstance(name, str):
        return abort(400)
    if len(text) == 0 or len(name) == 0:
        return abort(400)
    if len(text) > 1000 or len(name) > 100:
        return abort(400)

    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)

    if text == '/status':
        db.append({
            'text': 'On fire!!',
            'name': 'Ultra_Bot',
            'time': time.time()
        })

    if text == '/help':
        db.append({
            'text': "/status -- позволяет узнать статус Ультра_Бота,\n"
                    "/time -- узнать точное время,\n"
                    "/SilverName -- получи ссылку на лучшего стримера из России,\n"
                    "/joke -- почитать шутку про Python",
            'name': 'Ultra_Bot',
            'time': time.time()
        })

    if text == '/joke':
        translator = Translator(from_lang="en", to_lang="ru")
        joke = get_joke(category="all")
        db.append({
            'text': translator.translate(joke),
            'name': 'Ultra_Bot',
            'time': time.time()
        })

    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    result = []

    for message in db:
        if message['time'] > after:
            result.append(message)

    return {'messages': result[:100]}


app.run()
