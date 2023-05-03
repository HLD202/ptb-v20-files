import telebot

from decouple import config


bot = telebot.TeleBot(config('token'))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['video'])
def send_video(message: bot):
	    
    with open('video_file', 'rb') as f:
          video_file = f.read()

    bot.send_video(message.chat.id, video_file)




bot.infinity_polling()