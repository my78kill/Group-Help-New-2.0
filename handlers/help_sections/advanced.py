from telebot import types

def show(bot, call):

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back_help")
    )

    text = """
<b>Advanced Commands</b>

🕵🏻 Available to Admins  
👮🏻 Available to Admins & Moderators  
🛃 Available to Admins & Cleaners  

<b>⚠️ WARN MANAGEMENT</b>

👮🏻 /warn - adds a warn to the user  
👮🏻 /unwarn - removes a warn  
👮🏻 /warns - view/manage user warns  
🕵🏻 /delwarn - delete message & warn user  

🛃 /del - delete selected message  
🛃 /logdel - delete & send to log channel  

◽️ /me - sends your info in private chat  

🕵🏻 /send - send HTML post via bot  
➡️ Example: /send Hello World!  

👮🏻 /intervention - request official support help  
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )
