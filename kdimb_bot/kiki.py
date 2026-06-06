import os
import telebot
from threading import Thread

from kdimb_bot.flask_support.flask_sup import flask_thread

from kdimb_bot.core import *

from kdimb_bot.questions.strategies.antispam import register_handlers as register_antispam
from kdimb_bot.questions.strategies.quiz import register_handlers as register_quiz

START_MESSAGE = "Я Кики. Меня потеряли, ваша группа меня ищет? Добавьте меня туда. (Уверяю, мне можно доверить права администратора)"

@bot.message_handler(commands=['start'])
def cmd_start(message):
    print(f"[START] {message.from_user.first_name} (ID: {message.from_user.id})")
    bot.reply_to(message, START_MESSAGE)

register_antispam()
register_quiz()

# Запуск бота
if __name__ == '__main__':
    print("========================================")
    print("БУДИМ КИКИ")
    print("========================================")

    print("Попытка подключения к Telegram API...")
    try:
        bot_info = bot.get_me()
        print(f"УСПЕШНО! Вот и Кики: @{bot_info.username} (ID: {bot_info.id})")
    except Exception as e:
        print(f"НЕ УДАЛОСЬ подключиться: {e}")
        exit(1)

    bot.remove_webhook()
    bot.infinity_polling(timeout=60, long_polling_timeout=60)
