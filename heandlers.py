from loader import bot
import telebot


@bot.message_handler(commands=["start"])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Товар 1")
    btn2 = telebot.types.KeyboardButton("Товар 2")
    btn3 = telebot.types.KeyboardButton("Товар 3")
    btn4 = telebot.types.KeyboardButton("Связаться с проддержкой")
    markup.add(bnt1, btn2, btn3, btn4)
    text = f'Здравствуйте, {message.from_user.full_name}.\n' \
           f'Я ващ помощник в получении инструкций по товарам.\n' \
           f'По какому товару хотите получить инструкцию?.'
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)


@bot.message_handler(regexp='Товар 1')
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Вернуться к списку товаров")
    btn2 = telebot.types.KeyboardButton("Связаться с проддержкой")
    markup.add(bnt1, btn2)
    text = "Описание товара 1"
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
