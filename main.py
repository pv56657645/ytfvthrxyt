import telebot

tokin = '1749862558:AAEueIJsfOQ1FWlNDGtP5BunzAq77UsH7bg'

bot = telebot.TeleBot(tokin)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я великй стасик хуясик, я отвечу на все твои вопросы!')

@bot.message_handler(content_types=['text'])
def handle_text(message):

    bot.send_message(message.chat.id, "ДА!")

bot.polling(none_stop=True, interval=0)
