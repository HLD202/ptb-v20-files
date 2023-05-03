from decouple import config
tk = config('token')

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from telegram.ext import MessageHandler, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    args = context.args
    # print(args)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Hello, World',
        reply_to_message_id=update.effective_message.id)
    
"""
Your to do list:
    - cakelmrf
    - daefrktht
    - daefrktht
    - daefrktht

    [cakelmrf, cakelmrf, cakelmrf]
"""


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    txt = update.effective_message.text.split('\n')
    txt = '\n\t\t - '.join(txt)
    txt = f"Your To Do List: \n\t\t - {txt}"

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=txt,
        reply_to_message_id=update.effective_message.id)


dataBase = {
    "id": [],
    "name": [],
    "telephone": []
}

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE): ...

async def addUser(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    msg_id  = update.effective_message.id


    if len(args) != 2:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Error",
            reply_to_message_id=msg_id)


    elif user_id in dataBase['id']:
        await context.bot.send_message(
            chat_id=chat_id,
            text="User already is in DataBase, try another one",
            reply_to_message_id=msg_id)

    else:
        dataBase['id'].append(user_id)
        dataBase['name'].append(args[0])
        dataBase['telephone'].append(args[1])

        await context.bot.send_message(
            chat_id=chat_id,
            text="User has been added to dataBase",
            reply_to_message_id=msg_id)

        print(dataBase)


def main():
    app = Application.builder().token(tk).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    addUser_handler = CommandHandler('addUser', addUser)

    app.add_handler(start_handler)
    app.add_handler(addUser_handler)
    app.add_handler(echo_handler)

    app.run_polling()


if __name__=='__main__':
    main()
    
