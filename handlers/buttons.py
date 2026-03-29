from handlers.help_sections import basic
from handlers.help_sections import advanced
from handlers.help_sections import expert

# inside callback_handler

elif call.data == "basic":
    basic.show(bot, call)

elif call.data == "advanced":
    advanced.show(bot, call)

elif call.data == "expert":
    expert.show(bot, call)

elif call.data == "back_help":

    from telebot import types

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

    bot.edit_message_text(
        "📖 <b>Help Menu</b>\n\nChoose a category below:",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )
