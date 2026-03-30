from telebot import types
from handlers.help_sections import basic, advanced, expert, pro
from utils.db import get_groups
from utils.helpers import is_admin

def register(bot):

    # ================= SAFE EDIT FUNCTION =================
    def safe_edit(call, text, markup=None):
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

    # ================= SETTINGS COMMAND =================
    @bot.message_handler(commands=['settings'])
    def settings_cmd(message):

        # ===== GROUP =====
        if message.chat.type != "private":
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton(
                    "Open in Private 🔹",
                    url=f"https://t.me/{bot.get_me().username}?start=settings"
                )
            )

            bot.send_message(
                message.chat.id,
                "⚙️ Open settings in private chat.",
                reply_markup=markup
            )
            return

        # ===== PRIVATE =====
        groups = get_groups()
        markup = types.InlineKeyboardMarkup()
        found = False

        for chat_id, info in groups.items():
            if is_admin(bot, message.from_user.id, int(chat_id)):
                markup.add(
                    types.InlineKeyboardButton(
                        f"⚙️ {info['title']}",
                        callback_data=f"manage_{chat_id}"
                    )
                )
                found = True

        text = """
⚙️ <b>Manage Group Settings</b>

👉🏻 Select the group whose settings you want to change.

❗ If your group is not listed:
• Send /reload in the group and try again  
• Send /settings in the group and then press <b>Open in Pvt</b>
"""

        if not found:
            bot.send_message(
                message.chat.id,
                text + "\n\n❌ No groups found where you are admin."
            )
            return

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=markup
        )

    # ================= CALLBACK QUERY HANDLER =================
    @bot.callback_query_handler(func=lambda call: call.data is not None)
    def callback_handler(call):
        bot.answer_callback_query(call.id)

        # ================= HELP SECTIONS =================
        if call.data == "basic":
            basic.show(bot, call)

        elif call.data == "advanced":
            advanced.show(bot, call)

        elif call.data == "expert":
            expert.show(bot, call)

        elif call.data == "pro":
            pro.show(bot, call)

        elif call.data == "roles":
            pro.roles_menu(bot, call)

        elif call.data in pro.ROLE_GUIDES:
            pro.show_role_detail(bot, call)

        elif call.data == "back_help":
            markup = types.InlineKeyboardMarkup(row_width=2)

            markup.add(
                types.InlineKeyboardButton("👨‍🏫 Bot Configuration Tutorial 👨‍🏫", callback_data="tutorial")
            )

            markup.add(
                types.InlineKeyboardButton("👨 Basic", callback_data="basic"),
                types.InlineKeyboardButton("🧑 Advanced", callback_data="advanced")
            )

            markup.add(
                types.InlineKeyboardButton("🕵️ Expert", callback_data="expert"),
                types.InlineKeyboardButton("👨‍💼 Pro", callback_data="pro")
            )

            safe_edit(call, "📖 <b>Help Menu</b>\n\nChoose a category below:", markup)

        # ================= SETTINGS SYSTEM =================
        elif call.data == "settings":

            groups = get_groups()
            markup = types.InlineKeyboardMarkup()
            found = False

            for chat_id, info in groups.items():
                if is_admin(bot, call.from_user.id, int(chat_id)):
                    markup.add(
                        types.InlineKeyboardButton(
                            f"⚙️ {info['title']}",
                            callback_data=f"manage_{chat_id}"
                        )
                    )
                    found = True

            text = """
⚙️ <b>Manage Group Settings</b>

👉🏻 Select the group whose settings you want to change.

❗ If your group is not listed:
• Send /reload in the group and try again  
• Send /settings in the group and then press <b>Open in Pvt</b>
"""

            if not found:
                safe_edit(call, text + "\n\n❌ No groups found where you are admin.")
                return

            safe_edit(call, text, markup)

        elif call.data.startswith("manage_"):
            chat_id = call.data.split("_")[1]

            safe_edit(
                call,
                f"""
⚙️ <b>Managing Group</b>

🆔 <code>{chat_id}</code>

👉 Features coming next:
• Welcome settings  
• Anti-link  
• Moderation  

Stay tuned 🚀
"""
            )

        # ================= PRO GUIDES =================
        elif call.data == "setup_staff":
            safe_edit(call, "⚙️ Staff setup guide (Coming soon)")

        elif call.data == "clone":
            safe_edit(call, "🤖 Clone creation guide (Coming soon)")

        # ================= EXTRA =================
        elif call.data == "see_info":
            safe_edit(call, "ℹ️ More info coming soon...")

        # ================= DEFAULT =================
        else:
            safe_edit(call, "Feature coming soon...")

    # ================= GROUP JOIN HANDLER =================
    @bot.chat_member_handler()
    def bot_added(update):

        if update.new_chat_member and update.new_chat_member.user.id == bot.get_me().id:

            chat_id = update.chat.id

            if update.new_chat_member.status in ["administrator", "member"]:

                # ===== First message =====
                markup1 = types.InlineKeyboardMarkup()
                markup1.add(
                    types.InlineKeyboardButton(
                        "Subscribe My Channel",
                        url="https://t.me/YourChannel"
                    )
                )

                bot.send_message(
                    chat_id,
                    "Thank you for adding me to your group as an Administrator!\n"
                    "Start me in private chat, so I can send you the error messages there, without obstructing this chat!",
                    reply_markup=markup1
                )

                # ===== Second message =====
                markup2 = types.InlineKeyboardMarkup(row_width=2)
                markup2.add(
                    types.InlineKeyboardButton("See 👀", callback_data="see_info"),
                    types.InlineKeyboardButton("Settings", callback_data="settings")
                )

                bot.send_message(
                    chat_id,
                    "In order to set me up, use /settings or press the underlying button.",
                    reply_markup=markup2
                )
