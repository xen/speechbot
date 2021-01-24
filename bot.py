from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters,
)

from voice import text_to_file

TOKEN = "1538910118:AAFYWKyyWxADVaOlHpDyE6Yr0p3oCCAB-yE"


def hello(update, context):
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


def help_handler(update, context):
    help_text = """Для того чтобы преобразовать текст в аудио используйте наш бот. Пришлите любой текст обычным сообщение и он превратится в аудио сообщение"""
    update.message.reply_text(help_text)


def reply(update, context):
    file_name = text_to_file(update.message.text)
    # update.message.reply_text("Проговорим текст: " + update.message.text)
    update.message.reply_voice(voice=open(file_name, "rb"))


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("help", help_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()
