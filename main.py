# main.py
from telebot import TeleBot
from config import TOKEN
from handlers import start, buttons, help
from alive import keep_alive

bot = TeleBot(TOKEN, parse_mode="HTML", threaded=True)

# Start Flask server
keep_alive()

# Register handlers
start.register(bot)
buttons.register(bot)
help.register(bot)

print("Bot + Web Alive Started...")

# Use allowed_updates here instead
bot.infinity_polling(allowed_updates=['message', 'callback_query', 'chat_member'])
