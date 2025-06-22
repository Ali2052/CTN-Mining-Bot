import telebot
import os
from pymongo import MongoClient
from flask import Flask
from threading import Thread

# Bot token and DB URI (hardcoded here for your case)
BOT_TOKEN = "8005841394:AAFqiQTdJoBXVasZznYXhfr-31_DXSNdv-A"
MONGO_URI = "mongodb+srv://ContinentalCoin:%40%2FF03aliawan@continentalcoin.jrhsr0s.mongodb.net/"

# Initialize bot and MongoDB
bot = telebot.TeleBot(BOT_TOKEN)
client = MongoClient(MONGO_URI)
db = client["continental"]
users = db["users"]

# Telegram command
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "👋 Welcome to the CTN Mining Bot!\nClick every 12 hours to earn CTN!")

# Flask app (optional, for Render to detect port)
app = Flask(__name__)

@app.route('/')
def index():
    return "✅ CTN Mining Bot is running!"

# Run both Flask and Telegram bot
if __name__ == "__main__":
    def run_bot():
        bot.infinity_polling()

    Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)