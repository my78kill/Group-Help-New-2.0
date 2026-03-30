from telebot import TeleBot
from config import TOKEN
from handlers import start, help, buttons
from alive import keep_alive

bot = TeleBot(TOKEN, parse_mode="HTML", threaded=True)

keep_alive()

# ORDER IMPORTANT 🔥
start.register(bot)
help.register(bot)
buttons.register(bot)

print("Bot Started...")

bot.infinity_polling()
