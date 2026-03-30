from telebot import types

def register(bot):

    @bot.message_handler(commands=['help'])
    def help_cmd(message):
        if message.chat.type != "private":
            # Group → blue-link style
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton(
                    "Open Help Menu 🔹",
                    url=f"https://t.me/{bot.get_me().username}?start=help"
                )
            )
            bot.send_message(
                message.chat.id,
                "📘 <b>Commands Explanation</b>\n\nClick the button below to open the help menu in the bot.",
                reply_markup=markup
            )
        else:
            # Private chat → full buttons
            show_help_menu(bot, message)


def show_help_menu(bot, call_or_message):
    """Private chat /help menu with full buttons"""
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

    chat_id = call_or_message.chat.id
    message_id = getattr(call_or_message, "message_id", None)

    if message_id:  # callback query
        bot.edit_message_text(
            "📖 <b>Help Menu</b>\n\nChoose a category below:",
            chat_id,
            message_id,
            reply_markup=markup
        )
    else:  # normal message
        bot.send_message(
            chat_id,
            "📖 <b>Help Menu</b>\n\nChoose a category below:",
            reply_markup=markup
        )
