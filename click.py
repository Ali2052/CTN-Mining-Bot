import datetime
from database import get_user, update_user

def register(bot):
    @bot.message_handler(commands=['click'])
    def click_cmd(msg):
        user = get_user(msg.from_user.id)
        now = datetime.datetime.utcnow()
        if user.get("last_click") and (now - user["last_click"]).total_seconds() < 43200:
            bot.reply_to(msg, "⏳ You can click again in 12 hours!")
        else:
            new_balance = user["balance"] + 5
            update_user(msg.from_user.id, {"balance": new_balance, "last_click": now})
            bot.reply_to(msg, "✅ You mined 5 CTN!")
