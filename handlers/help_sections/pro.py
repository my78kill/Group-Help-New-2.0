from telebot import types

def show(bot, call):

    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton("⚙️ Setup Staff Group", callback_data="setup_staff"),
        types.InlineKeyboardButton("🤖 How to Create a Clone", callback_data="clone"),
        types.InlineKeyboardButton("👥 Users Roles", callback_data="roles"),
    )

    markup.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back_help")
    )

    text = """
<b>Pro Guides</b>

In this menu you will find some guides for very advanced Group Help functions.

⚠️ I recommend using them only if you know what you are doing  
and follow each step carefully.
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )
