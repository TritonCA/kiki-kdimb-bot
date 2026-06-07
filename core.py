import os
import telebot
from typing import Any
from dataclasses import dataclass, field

TOKEN = os.environ.get('BOT_TOKEN')
if TOKEN == None:
    try:
        TOKEN = open('secret_token.txt').read()
    except:
        TOKEN = "[CORE] Токен не найден"
        print(TOKEN)
bot = telebot.TeleBot(TOKEN)

BOT_ID: int = 0
CHAT_ID: int = 0
is_supergroup: bool = False

chats: dict[int, dict[str, Any]] = {}

def get_context(chat_id: int) -> dict[str, Any]:
    if chat_id not in chats:
        try:
            bot_id = bot.get_me().id
            chat = bot.get_chat(chat_id)
            
            chats[chat_id] = {
                'bot_id': bot_id,
                'is_supergroup': chat.type in ['supergroup', 'channel'],
                'title': chat.title or 'Личный чат'
            }
            print(f"Кики в чате: {chats[chat_id]['title']} (ID: {chat_id})")
            
        except Exception as e:
            print(f"Ошибка получения контекста чата: {e}")
            raise
    
    return chats[chat_id]