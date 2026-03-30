from telebot import types

def register(bot):

    @bot.message_handler(commands=['help'])
    def help_cmd(message):
        show_help_menu(bot, message)

# ===== Function to show help menu (can be called from buttons too) =====
def show_help_menu(bot, call_or_message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("👨‍🏫 Bot Configuration Tutorial 👨‍🏫", callback_data="tutorial")
    )

    markup.add(
        types.InlineKeyboardButton("👨 Basic", callback_data="basic"),
        types.InlineKeyboardButton("🧑 Advanced", callback_data="advanced")
    )

    markup.add(
        types.InlineKeyboardButton("🕵️ Expert", callback_data="expert"),
        types.InlineKeyboardButton("👨‍💼 Pro", callback_data="pro")
    )

    # Check if input is message or callback
    chat_id = call_or_message.chat.id
    message_id = getattr(call_or_message, "message_id", None)

    if message_id:  # If it's a callback query
        bot.edit_message_text(
            "📖 <b>Help Menu</b>\n\nChoose a category below:",
            chat_id,
            message_id,
            reply_markup=markup
        )
    else:  # If it's a normal message
        bot.send_message(
            chat_id,
            "📖 <b>Help Menu</b>\n\nChoose a category below:",
            reply_markup=markup
        )
