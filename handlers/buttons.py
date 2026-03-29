from handlers.help_sections import basic, advanced, expert, pro
from telebot import types

def register(bot):

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):

        bot.answer_callback_query(call.id)

        if call.data == "basic":
            basic.show(bot, call)

        elif call.data == "advanced":
            advanced.show(bot, call)

        elif call.data == "expert":
            expert.show(bot, call)

        elif call.data == "pro":
            pro.show(bot, call)

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

        elif call.data == "setup_staff":
            bot.edit_message_text("⚙️ Staff setup guide (Coming soon)", call.message.chat.id, call.message.message_id)

        elif call.data == "clone":
            bot.edit_message_text("🤖 Clone guide (Coming soon)", call.message.chat.id, call.message.message_id)

        elif call.data == "roles":
            bot.edit_message_text("👥 Roles guide (Coming soon)", call.message.chat.id, call.message.message_id)

        else:
            bot.edit_message_text(
                "Feature coming soon...",
                call.message.chat.id,
                call.message.message_id
            )
