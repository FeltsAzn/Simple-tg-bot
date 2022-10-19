from send_file import get_file_id
from loader import bot
from config import BOT_TOKEN, ADMIN_ID, ADMIN_NAME
import telebot
import aiohttp
import aiofiles

commads = ["Товар 1", "Товар 2", "Товар 3", "Связаться с поддержкой"]


@bot.message_handler(commands=["start"])
async def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Товар 1")
    btn2 = telebot.types.KeyboardButton("Товар 2")
    btn3 = telebot.types.KeyboardButton("Товар 3")
    btn4 = telebot.types.KeyboardButton("Связаться с поддержкой")
    markup.add(bnt1, btn2, btn3, btn4)
    text = f'Здравствуйте, {message.from_user.full_name}.\n' \
           f'Я ващ помощник в получении инструкций по товарам.\n' \
           f'По какому товару хотите получить инструкцию?.'
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)


@bot.message_handler(regexp='Товар 1')
async def product_one(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Товар 1")
    btn2 = telebot.types.KeyboardButton("Товар 2")
    btn3 = telebot.types.KeyboardButton("Товар 3")
    btn4 = telebot.types.KeyboardButton("Связаться с поддержкой")
    markup.add(bnt1, btn2, btn3, btn4)
    text = "Описание товара 1: "
    file_id = get_file_id("filename_1")
    if file_id:
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
        await bot.send_document(message.chat.id, file_id)
    else:
        file = open("product_instructions/Модели в Django. Лучшие практики .pdf", 'rb')
        await bot.send_document(message.chat.id, file)
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)


@bot.message_handler(regexp='Товар 2')
async def product_two(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Товар 1")
    btn2 = telebot.types.KeyboardButton("Товар 2")
    btn3 = telebot.types.KeyboardButton("Товар 3")
    btn4 = telebot.types.KeyboardButton("Связаться с поддержкой")
    markup.add(bnt1, btn2, btn3, btn4)
    text = "Описание товара 2: "
    file_id = get_file_id("filename_2")
    if file_id:
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
        await bot.send_document(message.chat.id, file_id)
    else:
        file = open("product_instructions/Cправочник_по_sql.pdf", 'rb')
        await bot.send_document(message.chat.id, file)
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)


@bot.message_handler(regexp='Товар 3')
async def product_three(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Товар 1")
    btn2 = telebot.types.KeyboardButton("Товар 2")
    btn3 = telebot.types.KeyboardButton("Товар 3")
    btn4 = telebot.types.KeyboardButton("Связаться с поддержкой")
    markup.add(bnt1, btn2, btn3, btn4)
    text = "Описание товара 3: "
    file_id = get_file_id("filename_3")
    if file_id:
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
        await bot.send_document(message.chat.id, file_id)
    else:
        file = open("product_instructions/Linux. syst.progr.2ed.pdf", 'rb')
        await bot.send_document(message.chat.id, file)
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)


@bot.message_handler(regexp='Связаться с поддержкой')
async def contact(message):
    text = f"https://t.me/{ADMIN_NAME}"
    await bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text not in commads, content_types=['text'])
async def invalid_command(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Товар 1")
    btn2 = telebot.types.KeyboardButton("Товар 2")
    btn3 = telebot.types.KeyboardButton("Товар 3")
    btn4 = telebot.types.KeyboardButton("Связаться с поддержкой")
    markup.add(bnt1, btn2, btn3, btn4)
    text = "Неверная команда."
    await bot.delete_message(chat_id=message.chat.id, message_id=message.id)
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)


# TODO сделать автоматическое сохранение файла на сервере и добавление токена доступа
@bot.message_handler(func=lambda mes: mes.from_user.id == ADMIN_ID,
                     content_types=["document", "video", "audio"])
async def handle_files(message):
    document_id = message.document.file_id
    file_info = await bot.get_file(document_id)
    print(document_id)  # Выводим file_id
    print(file_info)
    req = f'http://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_id}'
    async with aiohttp.ClientSession() as session:
        async with session.get(req) as resp:
            content = await resp.read()
            async with aiofiles.open('product_instructions/content.pdf', "+wb") as file:
                await file.write(content)

    await bot.send_message(message.chat.id, document_id)  # Отправляем пользователю file_id
