from telebot import types


# ================= MAIN PANEL =================
def show(bot, call, chat_id, group_name):
    """Main Settings Panel UI (for callback)"""

    markup = build_markup()

    text = f"""
⚙️ <b>SETTINGS</b>

🏷 Group: <b>{group_name}</b>

Select one of the settings that you want to change.
"""

    # ✅ SAFE EDIT
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


# ================= DIRECT OPEN (DM) =================
def direct_open(bot, user, chat_id, group_name):
    """Open settings directly in private chat"""

    markup = build_markup()

    text = f"""
⚙️ <b>SETTINGS</b>

🏷 Group: <b>{group_name}</b>

Select one of the settings that you want to change.
"""

    bot.send_message(
        user.id,
        text,
        reply_markup=markup
    )


# ================= BUTTON BUILDER =================
def build_markup():
    """Reusable buttons"""

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

    # center
    markup.add(
        types.InlineKeyboardButton("📥 Approval Mode", callback_data="set_approval")
    )

    markup.add(
        types.InlineKeyboardButton("🗑 Deleting Messages", callback_data="set_delete")
    )

    # bottom
    markup.add(
        types.InlineKeyboardButton("❌ Close", callback_data="close_settings"),
        types.InlineKeyboardButton("▶️ Other", callback_data="set_other")
    )

    return markup
