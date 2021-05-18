from bot import TelegramBot
from constants import TELEGRAM_BOT
from bot.message import TextMessage


def start(message):
    chat_id = message['message']['chat']['id']
    user_id = message['message']['from']['id']
    first_name = message['message']['from']['first_name']

    user_mention = TelegramBot.get_user_mention(user_id, first_name)

    TELEGRAM_BOT.send_message(
        TextMessage(f'{user_mention} Você está começando!!!'),
        chat_id
    )
