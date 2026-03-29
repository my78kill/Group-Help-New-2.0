from telebot import types

def register(bot):

    @bot.message_handler(commands=['help'])
    def help_cmd(message):

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton("👨‍🏫 Bot Configuration Tutorial 👨‍🏫", callback_data="tutorial")
        )

        markup.add(
            types.InlineKeyboardButton("👨 Basic commands", callback_data="basic"),
            types.InlineKeyboardButton("🧑 Advanced", callback_data="advanced")
        )

        markup.add(
            types.InlineKeyboardButton("🕵️ Experts", callback_data="expert"),
            types.InlineKeyboardButton("👨‍💼 Pro Guides", callback_data="pro")
        )

        bot.send_message(
            message.chat.id,
            "📖 <b>Welcome to the help menu!</b>",
            reply_markup=markup
        )
