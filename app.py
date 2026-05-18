import random
import requests
from flask import Flask, request

BOT_TOKEN = '8658765599:AAHQUjKZFP9v6Jtat_L5kAnKqjWTj0MXQJY'
pending_binds = {}

app = Flask(__name__)

@app.route('/getkey')
def get_key():
    chat_id = request.args.get('chat_id', '')
    nickname = request.args.get('nick', 'Игрок')
    if not chat_id:
        return "ERROR"
    key = random.randint(100000, 999999)
    pending_binds[str(key)] = {'chat_id': chat_id, 'nickname': nickname}
    return str(key)

@app.route('/confirm')
def confirm():
    key = request.args.get('key', '')
    player = request.args.get('player', '')
    if key in pending_binds:
        data = pending_binds[key]
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        msg = f"Аккаунт {player} привязан!"
        requests.post(url, data={'chat_id': data['chat_id'], 'text': msg})
        del pending_binds[key]
        return "OK"
    return "ERROR"

if __name__ == '__main__':
    app.run()