from telebot import TeleBot
from config import TOKEN
from handlers import start, buttons, help
from alive import keep_alive

bot = TeleBot(TOKEN, parse_mode="HTML")

# Start Flask server
keep_alive()

# Register handlers
start.register(bot)
buttons.register(bot)
help.register(bot)

print("Bot + Web Alive Started...")

bot.infinity_polling()
