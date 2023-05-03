# Goals:
#   
#   - forwardMessage
#   - editMessage
#   - Post
#   - file Protection
#   - timer -> python-telegram-bot[job-queue]

from decouple import config
tk = config('token')

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def remove_message(context: ContextTypes.DEFAULT_TYPE):
    Job = context.job

    await context.bot.delete_message(
        chat_id=Job.chat_id,
        message_id=Job.data
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    chat_id = update.effective_chat.id
    
    # await context.bot.send_message(update.effective_chat.id, 'start function')

    message_id = update.effective_message.id + 1

    await context.bot.forward_message(
        chat_id=chat_id,
        from_chat_id="@HLD202YTtutorial",
        message_id=4)

    # await context.bot.edit_message_text(
    #     text="Hello, World",
    #     chat_id="@HLD202YTtutorial",
    #     message_id=4
    #     )
    
    # await context.bot.send_message(
    #     chat_id="@HLD202YTtutorial",
    #     text="It's new Text"
    # )
    await update.message.reply_text("it's start function")

    time = 10
    context.job_queue.run_once(
        callback=remove_message,
        when=time,
        chat_id=chat_id,
        name=str(chat_id),
        data=message_id
    )


def main():
    app = Application.builder().token(tk).build()

    app.add_handlers([
        CommandHandler('start', start)
    ])

    app.run_polling(timeout=20)


if __name__=="__main__":
    main()