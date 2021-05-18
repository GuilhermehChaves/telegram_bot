from bot import TelegramBot
from bot.message import TextMessage

telegram_bot = TelegramBot('BOT_TOKEN')


def start(update):
    chat_id = update['message']['chat']['id']
    user_id = update['message']['from']['id']
    first_name = update['message']['from']['first_name']

    user_mention = TelegramBot.get_user_mention(user_id, first_name)

    telegram_bot.send_message(
        TextMessage(f'{user_mention} Você está começando!!!'),
        chat_id
    )


if __name__ == '__main__':
    telegram_bot.add_command("/start", start)
    telegram_bot.run()
