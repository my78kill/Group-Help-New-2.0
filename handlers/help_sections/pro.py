from telebot import types

# ================= ROLE DETAILS =================
ROLE_GUIDES = {
    "role_founder": """
👑 <b>Founder</b>
Founder is the group creator, with all the power from Telegram and from the Bot
➕ Appears first in the Staff list
➕ They can manage cofounders, moderators, helper, free users
➕ They can manage all the users, also admins

Founder can be changed, directly with Telegram system.
""",
    "role_cofounder": """
⚜ <b>Co-Founder</b>
They are Admins with extra power
➕ They appear in the Staff list
➕ They can set cofounders, moderators, helper, free users and they can ban them

Commands: /cofounder and /uncofounder
""",
    "role_admin": """
👮 <b>Admin</b>
➕ They appear in Staff list
➕ They can manage group /settings
➕ They can moderate users (from Telegram or with commands like /ban), if they have "Ban users" permission
➕ They can delete messages (from Telegram or with /del and /logdel), if they have "Delete messages" permission
➕ They can manage pinned messages (from Telegram or with commands like /pin), if they have "Pin messages" permission

There are 2 ways to add/remove them:
• using the commands /admin and /unadmin
• setting them from the administrators panel of the Telegram group and then using /reload in the group
""",
    "role_moderator": """
👷🏻‍♂️ <b>Moderator</b>
➕ They appear in the Staff list
➕ They can use all moderation commands from the bot
➕ They are free users
➖ They cannot delete messages

Commands: /mod and /unmod
""",
    "role_cleaner": """
🛃 <b>Chat Cleaner</b>
➕ They appear in the Staff list
➕ They can delete messages with /del or /logdel
➖ They cannot moderate users
➖ They aren't free by default

Commands: /cleaner and /uncleaner
""",
    "role_muter": """
🙊 <b>Muter</b>
➕ They can mute and unmute users
➕ They are free users
➖ They cannot ban/kick users
➖ They cannot delete messages

Commands: /muter and /unmuter
""",
    "role_helper": """
⛑ <b>Helper</b>
➕ They appear in Staff list
➖ They don't have any power
➖ They aren't free users

Commands: /helper and /unhelper
""",
    "role_free": """
🔓 <b>Free</b>
➕ The Bot ignores them for automatic punishment

Commands: /free and /unfree
"""
}

# ================= SAFE EDIT FUNCTION =================
def safe_edit(bot, call, text, markup):
    try:
        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    except:
        bot.send_message(
            call.message.chat.id,
            text,
            reply_markup=markup
        )

# ================= PRO MAIN MENU =================
def show(bot, call):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton("⚙️ Setup Staff Group", callback_data="setup_staff"),
        types.InlineKeyboardButton("🤖 How to Create a Clone", callback_data="clone"),
        types.InlineKeyboardButton("👥 Users Roles", callback_data="roles"),
    )

    markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_help"))

    text = """
<b>Pro Guides</b>

In this menu you will find some guides for very advanced Group Help functions.

⚠️ I recommend using them only if you know what you are doing  
and follow each step carefully.
"""

    safe_edit(bot, call, text, markup)

# ================= USERS ROLES MENU =================
def roles_menu(bot, call):
    markup = types.InlineKeyboardMarkup(row_width=2)

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

    markup.add(types.InlineKeyboardButton("🔙 Back to Guide", callback_data="pro"))

    text = """
👥 <b>Users Roles</b>

Use the inline keyboard to discover the power of roles!

To add or remove a role from a user you can use commands present in the role tabs or with /info -> ROLES.
"""

    safe_edit(bot, call, text, markup)

# ================= ROLE DETAILS =================
def show_role_detail(bot, call):
    if call.data in ROLE_GUIDES:

        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("🔙 Back to Roles", callback_data="roles")
        )

        safe_edit(bot, call, ROLE_GUIDES[call.data], markup)
