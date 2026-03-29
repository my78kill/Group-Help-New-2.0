from handlers.help_sections import basic, advanced, expert, pro

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
