import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

telegram_bot_token = "5099437040:AAETg-rRGvoSY10qDkFLn17kxUNMMCmlpBM"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello World")


dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()