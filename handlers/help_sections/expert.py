from telebot import types

def show(bot, call):

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back_help")
    )

    text = """
<b>Expert Commands</b>

👥 Available to all users  
👮🏻 Available to Admins & Moderators  
🕵🏻 Available to Admins  

👥 /geturl - reply to a message to get its direct link  

🕵🏻 /inactives [days] - get inactive users list in private  

<b>📌 Pinned Messages</b>

🕵🏻 /pin [message] - send & pin via bot  
🕵🏻 /pin - pin replied message  
🕵🏻 /editpin [message] - edit pinned message  
🕵🏻 /delpin - remove pinned message  
🕵🏻 /repin - re-pin with notification  
👥 /pinned - view current pinned message  

🕵🏻 /list - users list with message count  
🕵🏻 /list roles - list all special roles  

🕵🏻 /graphic - group activity graph  
🕵🏻 /trend - group growth statistics  
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )
