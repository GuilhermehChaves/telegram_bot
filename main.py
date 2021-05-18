from bot.message import TextMessage
from constants import TELEGRAM_BOT
from commands import start

from flask import Flask, Response, request

app = Flask(__name__)

# set webhook
# https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url=
# https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook


TELEGRAM_BOT.add_command('/start', start)


@app.route('/', methods=['POST'])
def handle_messages():
    message = request.get_json()
    is_command = TELEGRAM_BOT.verify_command(message)

    if not is_command:
        chat_id = message['message']['chat']['id']
        TELEGRAM_BOT.send_message(TextMessage('Olá eu sou um bot!!!'), chat_id)

    return Response('success', status=200)


if __name__ == '__main__':
    app.run(debug=True)
