from telebot import types
from handlers import help  # ensure help.py has show_help_menu(bot, message)

def register(bot):

    @bot.message_handler(commands=['start'])
    def start_cmd(message):
        chat_id = message.chat.id
        user_name = message.from_user.first_name

        # Check if there is a payload (like start=help)
        start_payload = message.text.split(maxsplit=1)
        payload = None
        if len(start_payload) > 1:
            payload = start_payload[1]

        # ==================== PRIVATE CHAT ====================
        if message.chat.type == "private":
            # If start payload is help → open help menu buttons
            if payload == "help":
                help.show_help_menu(bot, message)
                return

            # Normal private start
            bot_username = bot.get_me().username
            markup = types.InlineKeyboardMarkup(row_width=2)

            # Add buttons
            markup.add(
                types.InlineKeyboardButton(
                    "➕ Add me to a Group ➕",
                    url=f"https://t.me/{bot_username}?startgroup=true"
                )
            )
            markup.add(
                types.InlineKeyboardButton("⚙️ Manage Group Settings ✍️", callback_data="settings")
            )
            markup.add(
                types.InlineKeyboardButton("👥 Group", callback_data="group"),
                types.InlineKeyboardButton("📢 Channel", callback_data="channel")
            )
            markup.add(
                types.InlineKeyboardButton("🆘 Support", callback_data="support"),
                types.InlineKeyboardButton("ℹ️ Information", callback_data="info")
            )
            markup.add(
                types.InlineKeyboardButton("🌐 Languages 🌐", callback_data="lang")
            )

            bot.send_message(
                chat_id,
                f"✨ <b>Hey {user_name}!</b>\n\n"
                "🤖 I’m your smart Group Assistant\n\n"
                "🚀 Add me to your group & promote me as admin\n"
                "⚡ Tap <b>/help</b> to explore all features",
                reply_markup=markup
            )

        # ==================== GROUP CHAT ====================
        else:
            # Group /start
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

    # ==================== GROUP /start BUTTONS ====================
    @bot.callback_query_handler(func=lambda call: call.data.startswith("start_"))
    def start_buttons_handler(call):
        bot.answer_callback_query(call.id)
        chat_id = call.message.chat.id

        if call.data == "start_commands":
            # Redirect user to bot for help menu
            bot.send_message(
                chat_id,
                f"📘 <b>Commands Explanation</b>\n\n"
                "Click the button below to open the help menu in the bot.",
                reply_markup=types.InlineKeyboardMarkup().add(
                    types.InlineKeyboardButton(
                        "Open Help Menu 🔹",
                        url=f"https://t.me/{bot.get_me().username}?start=help"
                    )
                )
            )

        elif call.data == "start_settings":
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton("Open here", callback_data="settings_here"),
                types.InlineKeyboardButton("Open in private chat", callback_data="settings_private")
            )
            bot.edit_message_text(
                "Where do you want to open the settings menu?",
                chat_id,
                call.message.message_id,
                reply_markup=markup
            )

    # ==================== SETTINGS BUTTON CHOICES ====================
    @bot.callback_query_handler(func=lambda call: call.data.startswith("settings_"))
    def settings_buttons_handler(call):
        bot.answer_callback_query(call.id)
        chat_id = call.message.chat.id

        if call.data == "settings_here":
            bot.send_message(chat_id, "Opening settings here...")
            bot.send_message(chat_id, "⚙️ Use /settings to configure the group here.")

        elif call.data == "settings_private":
            bot.send_message(chat_id, "Please start a private chat with me to open settings.")
