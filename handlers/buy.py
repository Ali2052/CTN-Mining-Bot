from config import WALLET_ADDRESS, CTN_RATE

def register(bot):
    @bot.message_handler(commands=['buy'])
    def buy_cmd(msg):
        bot.send_message(msg.chat.id, f"""
🛒 To buy CTN before launch:

1️⃣ Send BNB to:
`{WALLET_ADDRESS}`

2️⃣ Rate: 1 USD = {CTN_RATE} CTN  
📌 After payment, send proof to admin.
        """, parse_mode="Markdown")
