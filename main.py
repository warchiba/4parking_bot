import telebot

bot = telebot.TeleBot('token')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Привет, это бот 4Parking!")

bot.polling(none_stop=True, interval=0)

