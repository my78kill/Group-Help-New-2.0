from telebot import types

def register(bot):

    @bot.message_handler(commands=['help'])
    def help_cmd(message):

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

        bot.send_message(
            message.chat.id,
            "📖 <b>Help Menu</b>\n\nChoose a category below:",
            reply_markup=markup
        )
