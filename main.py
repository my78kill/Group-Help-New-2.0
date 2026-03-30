from telebot import TeleBot
from config import TOKEN
from handlers import start, buttons, help
from alive import keep_alive

# Bot object with allowed_updates for chat_member events
bot = TeleBot(
    TOKEN,
    parse_mode="HTML",
    threaded=True,
    allowed_updates=['message', 'callback_query', 'chat_member']
)

# Start Flask server
keep_alive()

# Register handlers
start.register(bot)
buttons.register(bot)
help.register(bot)

print("Bot + Web Alive Started...")

bot.infinity_polling()
