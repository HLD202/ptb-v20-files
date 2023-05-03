from decouple import config

Tk = config('token')

from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hello, World", 
        reply_to_message_id=update.effective_message.id)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = "\n\t\t- ".join(update.message.text.split("\n"))

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="You said:\n\t\t- "+txt,
        reply_to_message_id=update.effective_message.id)


dataBase = {
    "name": [],
    "telephone": []}



def main():
    app = Application.builder().token(Tk).build()
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app.add_handler(start_handler)
    app.add_handler(echo_handler)

    app.run_polling()

if __name__=='__main__':
    main()