import telebot
from configuration import keys, ТОКЕН
from extensions import ConvertionException, MoneyConverter

бот = telebot.TeleBot('5211745042:AAHw6Ukgx9YWyyS4qh1jknaXmvkWrMKr8BA')

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n<название валюты> \
<в какую валюту конвертировать> \
<количество конвертируемой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
значения def(message: telebot.types.Message):
    text = 'Доступные валюты:'
    для ключа в keys.keys():
        text = '\n'.join((текст, ключ, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
 преобразование def(message: telebot.types.Message):
    попробуйте:
        значения = message.text.split(' ')

        если len(значения) != 3:
            raise ConvertionException('Недопустимое количество параметров.')

        quote, base, amount = значения
        total_base = MoneyConverter.convert(котировка, база, сумма)
    кроме ConvertionException как e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    кроме исключения как e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')

    ещё:

        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)



bot.polling()

