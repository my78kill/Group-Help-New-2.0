from telebot import types

def register(bot):

    @bot.message_handler(commands=['start'])
    def start_cmd(message):

        bot_username = bot.get_me().username

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton(
                "➕ Add me to a Group ➕",
                url=f"https://t.me/{bot_username}?startgroup=true"
            )
        )

        markup.add(
            types.InlineKeyboardButton("⚙️ Manage Group Settings ✍️", callback_data="settings")
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
✨ <b>Hey {message.from_user.first_name}!</b>

🤖 <b>I’m your smart Group Assistant</b>

🚀 Add me to your group & promote me as admin  
🛡️ I’ll help you manage, protect & automate everything  

⚡ Tap <b>/help</b> to explore all features
""",
            reply_markup=markup
        )
