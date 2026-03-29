def register(bot):

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):

        bot.answer_callback_query(call.id)

        if call.data == "settings":
            text = "⚙️ Group settings panel (Coming soon)"

        elif call.data == "group":
            text = "👥 Group options (Coming soon)"

        elif call.data == "channel":
            text = "📢 Channel options (Coming soon)"

        elif call.data == "support":
            text = "🆘 Support system (Coming soon)"

        elif call.data == "info":
            text = "ℹ️ Bot info (Coming soon)"

        elif call.data == "lang":
            text = "🌐 Language system (Coming soon)"

        elif call.data == "tutorial":
            text = "👨‍🏫 Tutorial section (Coming soon)"

        elif call.data == "basic":
            text = "👨 Basic commands list (Coming soon)"

        elif call.data == "advanced":
            text = "🧑 Advanced commands (Coming soon)"

        elif call.data == "expert":
            text = "🕵️ Expert tools (Coming soon)"

        elif call.data == "pro":
            text = "👨‍💼 Pro guides (Coming soon)"

        else:
            text = "Unknown option"

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id
        )
