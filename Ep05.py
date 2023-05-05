"""
    Goals:

        ~ callbackQuery
        ~ inlineQuery
"""

from decouple import config

Tk = config('token')

# -----< Basic Packages >----- #
from telegram import Update 
from telegram.ext import Application, CommandHandler, ContextTypes

# -----< Callback Query Packages >----- #
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

# ------< Inline Query Packages >------ #
from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from telegram.constants import ParseMode

# -----< Start Function >----- # 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keys = [
        [InlineKeyboardButton('Button 1', callback_data='1'), InlineKeyboardButton('Button 2', callback_data='2')],
        [InlineKeyboardButton('Button 3', callback_data='3'), InlineKeyboardButton('Button 4', callback_data='4')],
    ]

    mrkUP = InlineKeyboardMarkup(keys)

    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hello, World", 
        reply_to_message_id=update.effective_message.id,
        reply_markup=mrkUP)
    

# -----< Callback Query >----- #
async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    call_back_data = query.data

    print(call_back_data)

# ------< Inline Query >------ #
async def inline_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    query: str = update.inline_query.query
    if query == '':
        return
    

    result = [
        InlineQueryResultArticle(
            id=uuid4(),
            title='UPPER',
            input_message_content=InputTextMessageContent(message_text=query.upper()),
            description='This command will make the query Uppercase'
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title='lower',
            input_message_content=InputTextMessageContent(message_text=query.lower()),
            description='This command will make the query lowercase'
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title='BOLD',
            input_message_content=InputTextMessageContent(message_text=f"<b>{query}</b>", parse_mode=ParseMode.HTML),
            description='This command will make the query BOLD'
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title='Italic',
            input_message_content=InputTextMessageContent(message_text=f"<i>{query}</i>", parse_mode=ParseMode.HTML),
            description='This command will make the query Italic'
        )
        
    ]

    await context.bot.answer_inline_query(update.inline_query.id, results=result)


from telegram.ext import MessageHandler, filters
from json import dumps

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # msg = update.effective_message.to_dict()

    # with open('result.json', 'w') as f:
    #     f.write(dumps(msg, indent=4))

    chat_id = update.effective_chat.id
    txt = '<code>This is my</code> Text'
    

    await context.bot.send_message(
        chat_id=chat_id, 
        text=txt,
        parse_mode=ParseMode.HTML
        )
    
def main():
    app = Application.builder().token(Tk).build()

    app.add_handlers([
        CommandHandler(['start', 'help'], start),
        CallbackQueryHandler(callback_query_handler),
        InlineQueryHandler(inline_query_handler),
        MessageHandler(filters.TEXT, message_handler)
    ])

    app.run_polling()

if __name__=='__main__':
    main()