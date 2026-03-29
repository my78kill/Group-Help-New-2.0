from telebot import types

def show(bot, call):

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back_help")
    )

    text = """
<b>Base Commands</b>

👮🏻 Available to Admins & Moderators  
🕵🏻 Available to Admins  

👮🏻 /reload - updates the Admins list and their privileges  

🕵🏻 /settings - manage all the bot settings in a group  

👮🏻 /ban - ban a user permanently from the group  

👮🏻 /mute - put a user in read-only mode  

👮🏻 /kick - remove a user (can rejoin via link)  

👮🏻 /unban - remove user from blacklist  

👮🏻 /info - get user info  
👮🏻 /infopvt - get info in private  

◽️ /staff - list of group staff  

✨ Gudboi
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )
