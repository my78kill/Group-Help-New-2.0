from telebot import types
from handlers import help

def register(bot):

    @bot.message_handler(commands=['start'])
    def start_cmd(message):
        chat_id = message.chat.id
        user_name = message.from_user.first_name

        # ===== SAFE PAYLOAD =====
        payload = None
        if message.text:
            parts = message.text.split()
            if len(parts) > 1:
                payload = parts[1].lower()

        # ================= PRIVATE =================
        if message.chat.type == "private":

            # 🔥 ONLY exact help payload
            if payload == "help":
                help.show_help_menu(bot, message)
                return

            bot_username = bot.get_me().username

            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton(
                    "➕ Add me to a Group ➕",
                    url=f"https://t.me/{bot_username}?startgroup=true"
                )
            )

            markup.add(
                types.InlineKeyboardButton(
                    "⚙️ Manage Group Settings ✍️",
                    callback_data="settings"
                ),
                types.InlineKeyboardButton(
                    "👀 Bot Commands",
                    url=f"https://t.me/{bot_username}?start=help"
                )
            )

            bot.send_message(
                chat_id,
                f"✨ <b>Hey {user_name}!</b>\n\n"
                "🤖 I’m your smart Group Assistant\n\n"
                "🚀 Add me to your group & promote me as admin\n"
                "⚡ Tap <b>/help</b> to explore all features",
                reply_markup=markup
            )

        # ================= GROUP =================
        else:
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("Settings", callback_data="start_settings"),
                types.InlineKeyboardButton("Bot Commands", callback_data="start_commands")
            )

            bot.send_message(
                chat_id,
                f"Hello {user_name}!\n\n"
                "In order to set me up, use /settings or press the underlying button.",
                reply_markup=markup
            )

    # ================= GROUP BUTTONS =================
    @bot.callback_query_handler(func=lambda call: call.data.startswith("start_"))
    def start_buttons_handler(call):
        bot.answer_callback_query(call.id)

        chat_id = call.message.chat.id
        bot_username = bot.get_me().username

        if call.data == "start_commands":
            # 🔥 ALWAYS redirect to private help
            bot.send_message(
                chat_id,
                "📘 <b>Commands Explanation</b>\n\nClick below to open help menu.",
                reply_markup=types.InlineKeyboardMarkup().add(
                    types.InlineKeyboardButton(
                        "Open Help Menu 🔹",
                        url=f"https://t.me/{bot_username}?start=help"
                    )
                )
            )

        elif call.data == "start_settings":
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton(
                    "Open here",
                    callback_data="settings_here"
                ),
                types.InlineKeyboardButton(
                    "Open in private chat",
                    url=f"https://t.me/{bot_username}?start=settings"
                )
            )

            # 🔥 safe edit
            try:
                bot.edit_message_text(
                    "Where do you want to open the settings menu?",
                    chat_id,
                    call.message.message_id,
                    reply_markup=markup
                )
            except:
                bot.send_message(
                    chat_id,
                    "Where do you want to open the settings menu?",
                    reply_markup=markup
                )
