def show(bot, call):

    text = """
👨 <b>Basic Commands</b>

• /start - Start bot  
• /help - Open help menu  
• /settings - Open settings  

More coming soon...
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id
    )
