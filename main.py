import telebot
from config import TOKEN
from handlers import start, click, tap, buy, referral, task

bot = telebot.TeleBot(TOKEN)

start.register(bot)
click.register(bot)
tap.register(bot)
buy.register(bot)
referral.register(bot)
task.register(bot)

print("🤖 CTN Mining Bot Running...")
bot.infinity_polling()
