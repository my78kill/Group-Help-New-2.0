from telebot import TeleBot
from config import TOKEN
from handlers import start, buttons, help

bot = TeleBot(TOKEN, parse_mode="HTML")

start.register(bot)
buttons.register(bot)
help.register(bot)

print("Bot Running...")

bot.infinity_polling()
