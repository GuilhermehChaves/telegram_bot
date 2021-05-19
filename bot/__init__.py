import requests

from bot.message import Message, TextMessage


class TelegramBot:
    def __init__(self, token):
        self.base_url = f'https://api.telegram.org/bot{token}'
        self.commands = {}

    def send_message(self, msg: Message, chat_id: str) -> None:
        msg.send(chat_id, self.base_url)

    def add_command(self, name, action) -> None:
        self.commands[name] = action

    def set_webhook(self, url):
        path = '/setWebhook'
        webhook_uri = f'{self.base_url}{path}?url={url}'
        requests.get(webhook_uri)

    def delete_webhook(self):
        path = '/deleteWebhook'
        webhook_uri = f'{self.base_url}{path}'
        requests.get(webhook_uri)

    @staticmethod
    def get_user_mention(user_id, user_name) -> str:
        return f'<a href="tg://user?id={user_id}">@{user_name}</a>'

    def get_commands(self):
        return self.commands.keys()

    def verify_command(self, msg):
        if msg['message']['text'] is not None:
            text = msg['message']['text']

            if text in self.get_commands():
                action = self.commands[text]
                action(msg)

                return True

            return False

        return False
