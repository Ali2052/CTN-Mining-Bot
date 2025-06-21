from database import get_user

def register(bot):
    @bot.message_handler(commands=['referral'])
    def referral_cmd(msg):
        user = get_user(msg.from_user.id)
        ref_link = f"https://t.me/YourBotUsername?start={msg.from_user.id}"
        bot.send_message(msg.chat.id, f"""
🎁 Referral Program:

🔗 Your Link: {ref_link}
👥 Referrals: {user.get('referrals', 0)}

🎉 Rewards:
• 1 Referral = 5 CTN  
• 10 Referrals = 50 CTN  
• 50 Referrals = 250 CTN  
• 100 Referrals = 500 CTN  
        """)
