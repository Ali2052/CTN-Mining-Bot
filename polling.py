import telebot

# Add your bot token here
BOT_TOKEN = "8005841394:AAFqiQTdJoBXVasZznYXhfr-31_DXSNdv-A"

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the CTN Mining Bot!")

# Echo any text message
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

# Start infinite polling
print("Bot is running with infinite polling...")
bot.infinity_polling()
