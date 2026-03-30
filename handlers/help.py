from telebot import types

def register(bot):

    @bot.message_handler(commands=['help'])
    def help_cmd(message):

        # ===== GROUP =====
        if message.chat.type != "private":
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

        # ===== PRIVATE =====
        else:
            show_help_menu(bot, message)


def show_help_menu(bot, obj):
    """Help menu (works for both message & callback)"""

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

    text = "📖 <b>Help Menu</b>\n\nChoose a category below:"

    # ===== FIXED LOGIC =====
    if hasattr(obj, "message"):  # callback query
        try:
            bot.edit_message_text(
                text,
                obj.message.chat.id,
                obj.message.message_id,
                reply_markup=markup
            )
        except:
            bot.send_message(
                obj.message.chat.id,
                text,
                reply_markup=markup
            )
    else:  # normal message
        bot.send_message(
            obj.chat.id,
            text,
            reply_markup=markup
        )
