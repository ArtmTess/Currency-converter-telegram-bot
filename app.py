import telebot
from config import keys, TOKEN
from exceptions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def help(message: telebot.types.Message):
    text = "Hi! Welcome to Currency converter! For calculation currency exchange please type (by using 'space') values:" \
           ' \n- <Currency #1>  \n- <Currency #2 that should be converted to currency #1> \n - <Amount for currency amount #1. \n Example: us_dollar euro 100>\n \
List of Currencies: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Enter three parameters separated by a space')

        base, quote, amount = values
        total_base = CryptoConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Incorrect input. \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Failed to process command\n{e}')
    else:
        text = f'Requested: convert {amount} {base} to {quote}'\
               f'\n Result: {amount} {base} = {round(total_base,3)} {quote} \n'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
