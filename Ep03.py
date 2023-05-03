from decouple import config
tk = config('token')

from telegram import Update

from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram import ReplyKeyboardRemove

from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.ext import MessageHandler, filters


# ---- Start Command ---- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): 

    Synopsis = "After a horrific alchemy experiment goes wrong in the Elric household, brothers Edward and Alphonse are left in a catastrophic new reality. Ignoring the alchemical principle banning human transmutation, the boys attempted to bring their recently deceased mother back to life. Instead, they suffered brutal personal loss: Alphonse's body disintegrated while Edward lost a leg and then sacrificed an arm to keep Alphonse's soul in the physical realm by binding it to a hulking suit of armor."
    Synopsis = Synopsis[0:200] + '...'

    img_url = "https://cdn.myanimelist.net/images/anime/1208/94745l.jpg"

    # button_list = []
    # for i in range(1, 64, 2):
    #     button_list.append([
    #         InlineKeyboardButton(f'📥 Episode: {i:03} 📥', url='google.com'),
    #         InlineKeyboardButton(f'📥 Episode: {i+1:03} 📥', url='google.com'),
    #     ])

    button_list = [
        [KeyboardButton('hehe'), KeyboardButton('hoha')]
    ]

    mrk = ReplyKeyboardMarkup(button_list, resize_keyboard=True, one_time_keyboard=True)

    cap = f"""
🅾️ Anime: Fullmetal Alchemist: Brotherhood
📆 Aired: Apr 5, 2009 to Jul 4, 2010
📊 Score: 9.10
🗂 Episodes: 64
⛔️ Rating: R - 17+ (violence & profanity)

⭕️ {Synopsis}
"""

    with open('img.jpg', 'rb') as f:
        img = f.read()

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=img,
        caption=cap,
        # reply_markup=InlineKeyboardMarkup(button_list))
        reply_markup=ReplyKeyboardRemove())
        # reply_markup=ReplyKeyboardRemove())

    # await context.bot.send_message(
    #     chat_id=update.effective_chat.id,
    #     text='Hello, World',
    #     reply_to_message_id=update.effective_message.id,
    #     reply_markup=markup)
        

# ---- Initiate the Bot ---- #
def main():
    app = Application.builder().token(tk).build()

    
    app.add_handlers([
        CommandHandler('start', start)
    ])

    # ----< handlers >----

    app.run_polling()


if __name__=='__main__':
    main()