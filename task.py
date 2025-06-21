def register(bot):
    @bot.message_handler(commands=['tasks'])
    def task_cmd(msg):
        bot.send_message(msg.chat.id, """
📝 Complete these tasks and earn CTN:

✅ Follow Twitter — 10 CTN  
✅ Join Telegram — 5 CTN  
✅ Watch promo video — 10 CTN

Send screenshots to admin for rewards.
        """)
