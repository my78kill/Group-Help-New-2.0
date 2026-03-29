from telebot import types

def register(bot):

    @bot.message_handler(commands=['start'])
    def start_cmd(message):

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton("➕ Add me to a Group ➕", url="https://t.me/YOUR_BOT_USERNAME?startgroup=true")
        )

        markup.add(
            types.InlineKeyboardButton("⚙️ Manage group Settings ✍️", callback_data="settings")
        )

        markup.add(
            types.InlineKeyboardButton("👥 Group", callback_data="group"),
            types.InlineKeyboardButton("📢 Channel", callback_data="channel")
        )

        markup.add(
            types.InlineKeyboardButton("🆘 Support", callback_data="support"),
            types.InlineKeyboardButton("ℹ️ Information", callback_data="info")
        )

        markup.add(
            types.InlineKeyboardButton("🌐 Languages 🌐", callback_data="lang")
        )

        bot.send_message(
            message.chat.id,
            f"""
👋 <b>Hello {message.from_user.first_name}!</b>

🤖 <b>Welcome to My Group Help Bot</b>

👉 Add me in your group and make me admin  
👉 I will help you manage everything easily ⚡  

❓ Press /help to see all commands
""",
            reply_markup=markup
        )
