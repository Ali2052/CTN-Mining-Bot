from database import get_user

def register(bot):
    @bot.message_handler(commands=['start'])
    def start_cmd(msg):
        user = get_user(msg.from_user.id)
        bot.send_message(msg.chat.id, f"""
👋 Welcome to CTN Mining Bot!

💰 Balance: {user['balance']} CTN  
🕹 Commands:
➡️ /click - Mine every 12 hours  
➡️ /tap - Tap to earn  
➡️ /buy - Buy CTN before launch  
➡️ /referral - Invite friends  
➡️ /tasks - Complete tasks  
        """)
