import telebot

bot = telebot.TeleBot("5713410226:AAGYZ1g9P0X9kEPS5H5wd876-iJXRMksbo8", parse_mode=None)

print("Start")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
