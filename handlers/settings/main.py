from telebot import types


# ================= MAIN SETTINGS =================
def show(bot, call, chat_id, group_name):

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("📜 Regulation", callback_data="set_regulation"),
        types.InlineKeyboardButton("📩 Anti-Spam", callback_data="set_antispam")
    )

    markup.add(
        types.InlineKeyboardButton("💬 Welcome", callback_data="set_welcome"),
        types.InlineKeyboardButton("🌊 Anti-Flood", callback_data="set_antiflood")
    )

    markup.add(
        types.InlineKeyboardButton("👋 Goodbye", callback_data="set_goodbye"),
        types.InlineKeyboardButton("🔒 Blocks", callback_data="set_blocks")
    )

    markup.add(
        types.InlineKeyboardButton("📢 @Admins", callback_data="set_admins"),
        types.InlineKeyboardButton("🖼 Media", callback_data="set_media")
    )

    markup.add(
        types.InlineKeyboardButton("⚠️ Warns", callback_data="set_warns"),
        types.InlineKeyboardButton("🔗 Link", callback_data="set_link")
    )

    markup.add(
        types.InlineKeyboardButton("📥 Approval Mode", callback_data="set_approval")
    )

    markup.add(
        types.InlineKeyboardButton("🗑 Deleting Messages", callback_data="set_delete")
    )

    markup.add(
        types.InlineKeyboardButton("❌ Close", callback_data="close_settings"),
        types.InlineKeyboardButton("▶️ Other", callback_data="set_other")
    )

    text = f"""
⚙️ <b>SETTINGS</b>

🏷 Group: <b>{group_name}</b>

Select one of the settings that you want to change.
"""

    safe_edit(bot, call, text, markup)


# ================= REGULATION =================
def regulation_menu(bot, call):

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("✍️ Customize Messages", callback_data="reg_custom"),
        types.InlineKeyboardButton("🕹️ Commands Permission", callback_data="reg_permission"),
        types.InlineKeyboardButton("🔙 Back", callback_data="back_settings")
    )

    text = """
📜 <b>Group's regulations</b>

From this menu you can manage the group's regulations, that will be shown with the command /rules.

To edit who can use the /rules command, go to the "Commands permissions" section.
"""

    safe_edit(bot, call, text, markup)


# ================= ANTI SPAM =================
def antispam_menu(bot, call):

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📘 Telegram Links", callback_data="spam_links"),
        types.InlineKeyboardButton("📨 Forwarding", callback_data="spam_forward")
    )
    markup.add(
        types.InlineKeyboardButton("⛓️ Total Links Block", callback_data="spam_total")
    )
    markup.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back_settings")
    )

    text = """
📨 <b>Anti-Spam</b>

In this menu you can decide whether to protect your groups from unnecessary links, forwards, and quotes.
"""

    safe_edit(bot, call, text, markup)


# ================= WELCOME =================
def welcome_menu(bot, call):

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("❌ Turn off", callback_data="wel_off"),
        types.InlineKeyboardButton("☑️ Turn on", callback_data="wel_on")
    )
    markup.add(
        types.InlineKeyboardButton("✍️ Customize Message", callback_data="wel_custom")
    )
    markup.add(
        types.InlineKeyboardButton("♻️ Delete Last Message", callback_data="wel_delete")
    )
    markup.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back_settings")
    )

    text = """
💬 <b>Welcome Message</b>

From this menu you can set a welcome message that will be sent when someone joins the group.

Status: Off ❌  
Mode: Send the welcome message at every join of the users in the group
"""

    safe_edit(bot, call, text, markup)


# ================= GOODBYE =================
def goodbye_menu(bot, call):

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("❌ Turn off", callback_data="bye_off"),
        types.InlineKeyboardButton("☑️ Turn on", callback_data="bye_on")
    )
    markup.add(
        types.InlineKeyboardButton("✍️ Customize Messages", callback_data="bye_custom")
    )
    markup.add(
        types.InlineKeyboardButton("♻️ Delete Last Message", callback_data="bye_delete")
    )
    markup.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back_settings")
    )

    text = """
👋🏻 <b>Goodbye</b>

From this menu you can set a goodbye message that will be sent when someone leaves the group.

Status: Off ❌
"""

    safe_edit(bot, call, text, markup)


# ================= DELETE MENU =================
def delete_menu(bot, call, group_name):

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🤖 Commands", callback_data="del_commands"),
        types.InlineKeyboardButton("💭 Service Messages", callback_data="del_service")
    )
    markup.add(
        types.InlineKeyboardButton("🔥 Delete All Messages", callback_data="del_all")
    )
    markup.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back_settings")
    )

    text = """
🗑 <b>Deleting Messages</b>

What messages do you want the Bot to delete?
"""

    safe_edit(bot, call, text, markup)


# ================= OTHER MENU =================
def other_menu(bot, call, group_name):

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🔤 Banned Words", callback_data="set_banned"),
        types.InlineKeyboardButton("👥 Members Management", callback_data="set_members")
    )
    markup.add(
        types.InlineKeyboardButton("📏 Message Length", callback_data="set_length"),
        types.InlineKeyboardButton("🔍 Log Channel", callback_data="set_log")
    )
    markup.add(
        types.InlineKeyboardButton("🔏 Permission", callback_data="set_permission")
    )
    markup.add(
        types.InlineKeyboardButton("🔙 Back", callback_data="back_settings"),
        types.InlineKeyboardButton("❌ Close", callback_data="close_settings")
    )

    text = f"""
⚙️ <b>SETTINGS</b>

🏷 Group: <b>{group_name}</b>

Select one of the settings that you want to change.
"""

    safe_edit(bot, call, text, markup)


# ================= SAFE EDIT =================
def safe_edit(bot, call, text, markup=None):
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
