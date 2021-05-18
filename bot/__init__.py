import sys
import time

from bot.message import Message, TextMessage
from bot.updates import Updates


class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{self.token}'

    def send_message(self, msg: Message, chat_id: str) -> None:
        msg.send(chat_id, self.base_url)

    def run(self) -> None:
        while True:
            update_messages = Updates.get_update_messages(self.base_url)
            latest_update_id = ""

            try:
                for i, item in enumerate(update_messages['result']):
                    if i != 0:
                        chat_id = item['message']['chat']['id']
                        user_id = item['message']['from']['id']
                        user_name = item['message']['from']['first_name']
                        user_message = item['message']['text']

                        bot_message = f'<a href="tg://user?id={user_id}">@{user_name}</a> {user_message}'

                        self.send_message(TextMessage(bot_message), chat_id)

                        latest_update_id = item['update_id']

            except KeyboardInterrupt:
                sys.exit()

            Updates.clear_replied_messages(self.base_url, latest_update_id)
            time.sleep(0.5)
