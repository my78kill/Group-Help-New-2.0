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


def roles_menu(bot, call):
    """Users Roles button ka content aur buttons"""

    markup = types.InlineKeyboardMarkup(row_width=2)

    # Role pairs
    markup.add(
        types.InlineKeyboardButton("Founder", callback_data="role_founder"),
        types.InlineKeyboardButton("Co-Founder", callback_data="role_cofounder")
    )
    markup.add(
        types.InlineKeyboardButton("Admin", callback_data="role_admin"),
        types.InlineKeyboardButton("Moderator", callback_data="role_moderator")
    )
    markup.add(
        types.InlineKeyboardButton("Chat Cleaner", callback_data="role_cleaner"),
        types.InlineKeyboardButton("Muter", callback_data="role_muter")
    )
    markup.add(
        types.InlineKeyboardButton("Helper", callback_data="role_helper"),
        types.InlineKeyboardButton("Free", callback_data="role_free")
    )

   
    # Back to guide button
    markup.add(types.InlineKeyboardButton("🔙 Back to Guide", callback_data="pro"))

    # Message text upar
    text = """
👥 <b>Users Roles</b>

Use the inline keyboard to discover the power of roles!

To add or remove a role from a user you can use commands present in the role tabs or with /info -> ROLES.
"""

    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )
