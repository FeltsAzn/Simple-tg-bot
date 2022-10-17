from send_file import get_file_id
from loader import bot
import telebot
from config import URL, BOT_TOKEN


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
    text = "Описание товара 1: "
    file_id = get_file_id("filename_1")
    if file_id:
        bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
        bot.send_document(message.chat.id, file_id)


@bot.message_handler(regexp='Товар 2')
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Вернуться к списку товаров")
    btn2 = telebot.types.KeyboardButton("Связаться с проддержкой")
    markup.add(bnt1, btn2)
    text = "Описание товара 2: "
    file_id = get_file_id("filename_2")
    if file_id:
        bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
        bot.send_document(message.chat.id, file_id)


@bot.message_handler(regexp='Товар 3')
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Вернуться к списку товаров")
    btn2 = telebot.types.KeyboardButton("Связаться с проддержкой")
    markup.add(bnt1, btn2)
    text = "Описание товара 3: "
    file_id = get_file_id("filename_3")
    if file_id:
        bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
        bot.send_document(message.chat.id, file_id)


@bot.message_handler(regexp="Вернуться к списку товаров")
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Товар 1")
    btn2 = telebot.types.KeyboardButton("Товар 2")
    btn3 = telebot.types.KeyboardButton("Товар 3")
    btn4 = telebot.types.KeyboardButton("Связаться с проддержкой")
    markup.add(bnt1, btn2, btn3, btn4)
    text = "Возвращаюсь к списку товаров"
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)


@bot.message_handler(content_types=["document", "video", "audio"])
def handle_files(message):
  document_id = message.document.file_id
  file_info = bot.get_file(document_id)
  print(document_id) # Выводим file_id
  print(f'http://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}') # Выводим ссылку на файл
  bot.send_message(message.chat.id, document_id) # Отправляем пользователю file_id