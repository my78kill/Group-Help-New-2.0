def is_group(chat_id):
    return str(chat_id).startswith("-100")


def is_admin(bot, user_id, chat_id):
    try:
        admins = bot.get_chat_administrators(chat_id)
        return any(admin.user.id == user_id for admin in admins)
    except Exception as e:
        print("Admin check error:", e)
        return False
