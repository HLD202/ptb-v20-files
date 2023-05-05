from decouple import config
Tk = config('token')

from telegram import Update 
from telegram.ext import Application, CommandHandler, ContextTypes


# -----< Start Function >----- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hello, World", 
        reply_to_message_id=update.effective_message.id)
    

# -----< Initialize the Bot >----- #
def main():
    app = Application.builder().token(Tk).build()
    app.add_handlers([
        CommandHandler(['start', 'help'], start),
        # -----< add the rest of handlers >----- #
        
    ])

    app.run_polling()


if __name__=='__main__':
    main()