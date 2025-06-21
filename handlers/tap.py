from database import get_user, update_user

def register(bot):
    @bot.message_handler(commands=['tap'])
    def tap_cmd(msg):
        user = get_user(msg.from_user.id)
        new_balance = user["balance"] + 0.0001
        update_user(msg.from_user.id, {"balance": new_balance})
        bot.reply_to(msg, f"🖱 Tap registered! Earned 0.0001 CTN.\nTotal: {round(new_balance, 4)} CTN")
