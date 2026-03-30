from telebot import types
from handlers.settings import main as settings_main
from utils.db import get_groups, add_group
from utils.helpers import is_admin


def register(bot):

    # ================= SAFE EDIT =================
    def safe_edit(call, text, markup=None):
        try:
            bot.edit_message_text(
                text,
                call.message.chat.id,
                call.message.message_id,
                reply_markup=markup,
                parse_mode="HTML"
            )
        except:
            bot.send_message(
                call.message.chat.id,
                text,
                reply_markup=markup,
                parse_mode="HTML"
            )

    # ================= /SETTINGS =================
    @bot.message_handler(commands=['settings'])
    def settings_cmd(message):

        if message.chat.type != "private":
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("Open here", callback_data="settings_here"),
                types.InlineKeyboardButton("Open in private chat", callback_data="settings_private")
            )
            bot.send_message(message.chat.id, "Where do you want to open settings?", reply_markup=markup)
            return

        groups = get_groups()
        markup = types.InlineKeyboardMarkup()
        found = False

        for chat_id, info in groups.items():
            if is_admin(bot, message.from_user.id, int(chat_id)):
                markup.add(types.InlineKeyboardButton(
                    f"⚙️ {info['title']}",
                    callback_data=f"manage_{chat_id}"
                ))
                found = True

        if not found:
            bot.send_message(message.chat.id, "❌ No groups found where you are admin.")
            return

        bot.send_message(message.chat.id, "⚙️ Select a group:", reply_markup=markup)

    # ================= CALLBACK =================
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        bot.answer_callback_query(call.id)

        chat_id = call.message.chat.id
        group_name = call.message.chat.title

        # ===== OPEN =====
        if call.data == "settings_here":
            settings_main.show(bot, call, chat_id, group_name)

        elif call.data == "settings_private":
            bot_username = bot.get_me().username
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(
                "Open in DM 🔹",
                url=f"https://t.me/{bot_username}?start=settings_{chat_id}"
            ))
            safe_edit(call, "✅ Open in private chat.", markup)

        elif call.data.startswith("manage_"):
            gid = call.data.split("_")[1]
            gname = get_groups().get(gid, {}).get("title", "Unknown")
            settings_main.show(bot, call, gid, gname)

        elif call.data == "back_settings":
            settings_main.show(bot, call, chat_id, group_name)

        # ================= DELETE MENU =================
        elif call.data == "set_delete":

            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("🤖 Commands", callback_data="del_commands"),
                types.InlineKeyboardButton("💭 Service Messages", callback_data="del_service")
            )
            markup.add(
                types.InlineKeyboardButton("🔥 Delete all messages", callback_data="del_all")
            )
            markup.add(
                types.InlineKeyboardButton("🔙 Back", callback_data="back_settings")
            )

            text = """🗑 <b>Deleting Messages</b>

What messages do you want the Bot to delete?"""
            safe_edit(call, text, markup)

        # ================= OTHER MENU =================
        elif call.data == "set_other":

            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("🔤 Banned words", callback_data="set_banned"),
                types.InlineKeyboardButton("👥 Members management", callback_data="set_members")
            )
            markup.add(
                types.InlineKeyboardButton("📏 Message length", callback_data="set_length"),
                types.InlineKeyboardButton("🔍 Log channel", callback_data="set_log")
            )
            markup.add(
                types.InlineKeyboardButton("🔏 Permission", callback_data="set_permission")
            )
            markup.add(
                types.InlineKeyboardButton("🔙 Back", callback_data="back_settings"),
                types.InlineKeyboardButton("❌ Close", callback_data="close_settings")
            )

            text = f"""⚙️ <b>SETTINGS</b>

🏷 Group: <b>{group_name}</b>

Select one of the settings that you want to change."""
            safe_edit(call, text, markup)

        # ================= REGULATION =================
        elif call.data == "set_regulation":

            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("✍️ Customize Messages", callback_data="set_reg_msg"),
                types.InlineKeyboardButton("🕹️ Commands Permission", callback_data="set_reg_perm"),
                types.InlineKeyboardButton("🔙 Back", callback_data="back_settings")
            )

            text = """📜 <b>Group's regulations</b>

From this menu you can manage the group's regulations, that will be shown with the command /rules.

To edit who can use the /rules command, go to the "Commands permissions" section."""
            safe_edit(call, text, markup)

        # ================= ANTI-SPAM =================
        elif call.data == "set_antispam":

            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("📘 Telegram links", callback_data="set_spam_links"),
                types.InlineKeyboardButton("📨 Forwarding", callback_data="set_spam_forward")
            )
            markup.add(types.InlineKeyboardButton("⛓️ Total links block", callback_data="set_spam_total"))
            markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_settings"))

            text = """📨 <b>Anti-Spam</b>

In this menu you can decide whether to protect your groups from unnecessary links, forwards, and quotes."""
            safe_edit(call, text, markup)

        # ================= WELCOME =================
        elif call.data == "set_welcome":
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("❌ Turn off", callback_data="set_welcome_off"),
                types.InlineKeyboardButton("☑️ Turn on", callback_data="set_welcome_on")
            )
            markup.add(types.InlineKeyboardButton("✍️ Customize message", callback_data="set_welcome_msg"))
            markup.add(types.InlineKeyboardButton("♻️ Delete last message ❌", callback_data="set_welcome_delete"))
            markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_settings"))

            text = """💬 <b>Welcome Message</b>

From this menu you can set a welcome message that will be sent when someone joins the group.

Status: Off ❌
Mode: Send the welcome message at every join of the users in the group"""
            safe_edit(call, text, markup)

        # ================= GOODBYE =================
        elif call.data == "set_goodbye":
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("❌ Turn off", callback_data="set_goodbye_off"),
                types.InlineKeyboardButton("☑️ Turn on", callback_data="set_goodbye_on")
            )
            markup.add(types.InlineKeyboardButton("✍️ Customize messages", callback_data="set_goodbye_msg"))
            markup.add(types.InlineKeyboardButton("♻️ Delete last message", callback_data="set_goodbye_delete"))
            markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_settings"))

            text = """👋🏻 <b>Goodbye</b>

From this menu you can set a goodbye message that will be sent when someone leaves the group.

Status: Off ❌"""
            safe_edit(call, text, markup)

        # ================= BLOCKS =================
        elif call.data == "set_blocks":
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("❌ Turn off", callback_data="block_off"),
                types.InlineKeyboardButton("☑️ Turn on", callback_data="block_on")
            )
            markup.add(
                types.InlineKeyboardButton("🔇 Mute", callback_data="block_mute"),
                types.InlineKeyboardButton("🚫 Ban", callback_data="block_ban")
            )
            markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_settings"))

            text = """🤖 <b>Bot block</b>

If you enable this feature, users will not be able to add bots to the group.

Status: Active (Penalty: Off)"""
            safe_edit(call, text, markup)

        # ================= ADMINS =================
        elif call.data == "set_admins":
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("❌ Nobody", callback_data="admin_none"),
                types.InlineKeyboardButton("👑 Founder", callback_data="admin_founder")
            )
            markup.add(
                types.InlineKeyboardButton("🔔 Tag founder", callback_data="admin_tag_f"),
                types.InlineKeyboardButton("🔔 Tag admins", callback_data="admin_tag_a")
            )
            markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_settings"))

            text = """🆘 <b>@admin command</b>

@admin (or /report) is used by users to call admins.

Status: Active
Send to: 👑 Founder"""
            safe_edit(call, text, markup)

        # ================= ANTIFLOOD =================
        elif call.data == "set_antiflood":
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("📄 Messages", callback_data="af_msg"),
                types.InlineKeyboardButton("⏱️ Time", callback_data="af_time")
            )
            markup.add(
                types.InlineKeyboardButton("❌ Off", callback_data="af_off"),
                types.InlineKeyboardButton("🔇 Mute", callback_data="af_mute")
            )
            markup.add(
                types.InlineKeyboardButton("🚫 Ban", callback_data="af_ban"),
                types.InlineKeyboardButton("🗑️ Delete message ☑️", callback_data="af_delete")
            )
            markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_settings"))

            text = """🗣 <b>Antiflood</b>

Triggered when 5 messages in 3 seconds.

Punishment: Deletion"""
            safe_edit(call, text, markup)

        # ================= WARNS =================
        elif call.data == "set_warns":
            markup = types.InlineKeyboardMarkup(row_width=3)
            markup.add(
                types.InlineKeyboardButton("❌ Off", callback_data="warn_off"),
                types.InlineKeyboardButton("🔇 Mute", callback_data="warn_mute"),
                types.InlineKeyboardButton("🔇⏱️ Set mute duration", callback_data="warn_time")
            )
            markup.add(
                types.InlineKeyboardButton("2", callback_data="warn_2"),
                types.InlineKeyboardButton("3 ☑️", callback_data="warn_3"),
                types.InlineKeyboardButton("4", callback_data="warn_4"),
                types.InlineKeyboardButton("5", callback_data="warn_5"),
                types.InlineKeyboardButton("6", callback_data="warn_6")
            )
            markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_settings"))

            text = """❗️ <b>User warnings</b>

Punishment: Mute
Max Warns allowed: 3"""
            safe_edit(call, text, markup)

        # ================= LINK =================
        elif call.data == "set_link":
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("Set ✍️", callback_data="link_set"),
                types.InlineKeyboardButton("🔙 Back", callback_data="back_settings")
            )

            text = """🔗 <b>Group link</b>

Set your group link.

Status: Deactivated"""
            safe_edit(call, text, markup)

        elif call.data == "close_settings":
            safe_edit(call, "❌ Closed")

        else:
            safe_edit(call, "⚙️ Coming soon...")

    # ================= BOT ADDED =================
    @bot.chat_member_handler()
    def bot_added(update):
        if update.new_chat_member and update.new_chat_member.user.id == bot.get_me().id:
            add_group(update.chat.id, update.chat.title)
            bot.send_message(update.chat.id, "✅ Bot added! Use /settings")
