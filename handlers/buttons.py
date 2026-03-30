from telebot import types
from handlers.help_sections import basic, advanced, expert, pro
from utils.db import get_groups
from utils.helpers import is_admin

def register(bot):

    @bot.callback_query_handler(func=lambda call: True)
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

        # Role details
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

            bot.edit_message_text(
                "📖 <b>Help Menu</b>\n\nChoose a category below:",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=markup
            )

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
                bot.edit_message_text(
                    text + "\n\n❌ No groups found where you are admin.",
                    call.message.chat.id,
                    call.message.message_id
                )
                return

            bot.edit_message_text(
                text,
                call.message.chat.id,
                call.message.message_id,
                reply_markup=markup
            )

        elif call.data.startswith("manage_"):

            chat_id = call.data.split("_")[1]

            bot.edit_message_text(
                f"""
⚙️ <b>Managing Group</b>

🆔 <code>{chat_id}</code>

👉 Features coming next:
• Welcome settings  
• Anti-link  
• Moderation  

Stay tuned 🚀
""",
                call.message.chat.id,
                call.message.message_id
            )

        # ================= PRO GUIDES =================

        elif call.data == "setup_staff":
            bot.edit_message_text(
                "⚙️ Staff setup guide (Coming soon)",
                call.message.chat.id,
                call.message.message_id
            )

        elif call.data == "clone":
            bot.edit_message_text(
                "🤖 Clone creation guide (Coming soon)",
                call.message.chat.id,
                call.message.message_id
            )

        # ================= DEFAULT =================

        else:
            bot.edit_message_text(
                "Feature coming soon...",
                call.message.chat.id,
                call.message.message_id
            )
