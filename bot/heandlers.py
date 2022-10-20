from send_file import get_file_id, download_new_document
from loader import bot
from config import ADMIN_ID, ADMIN_NAME
import telebot
import json
from json.decoder import JSONDecodeError


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
    file_id: str | None = get_file_id("filename_1")
    if file_id is not None:
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
        await bot.send_document(message.chat.id, file_id)
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text="Ошибка отправки инструкции,\n"
                                    "пожалуйста обратитесь к поддержке!",
                               reply_markup=markup)


@bot.message_handler(regexp='Товар 2')
async def product_two(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Товар 1")
    btn2 = telebot.types.KeyboardButton("Товар 2")
    btn3 = telebot.types.KeyboardButton("Товар 3")
    btn4 = telebot.types.KeyboardButton("Связаться с поддержкой")
    markup.add(bnt1, btn2, btn3, btn4)
    text = "Описание товара 2: "
    file_id: str | None = get_file_id("filename_2")
    if file_id is not None:
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
        await bot.send_document(message.chat.id, file_id)
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text="Ошибка отправки инструкции,\n"
                                    "пожалуйста обратитесь к поддержке!",
                               reply_markup=markup)


@bot.message_handler(regexp='Товар 3')
async def product_three(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bnt1 = telebot.types.KeyboardButton("Товар 1")
    btn2 = telebot.types.KeyboardButton("Товар 2")
    btn3 = telebot.types.KeyboardButton("Товар 3")
    btn4 = telebot.types.KeyboardButton("Связаться с поддержкой")
    markup.add(bnt1, btn2, btn3, btn4)
    text = "Описание товара 3: "
    file_id: str | None = get_file_id("filename_3")
    if file_id is not None:
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)
        await bot.send_document(message.chat.id, file_id)
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text="Ошибка отправки инструкции,\n"
                                    "пожалуйста обратитесь к поддержке!",
                               reply_markup=markup)


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


@bot.message_handler(func=lambda mes: mes.from_user.id == ADMIN_ID,
                     content_types=["document", "video", "audio"])
async def handle_files(message):
    """Получаем документ от администратора для отправки на сервер"""
    document_id = message.document.file_id
    file_info = await bot.get_file(document_id)

    try:
        with open('product_instructions/file_id.json', mode="r", encoding='utf-8') as json_file:
            filenames: dict = json.load(json_file)
    except FileNotFoundError:
        """Если файл у нас не существует (удален), создается новый файл"""
        file = open('product_instructions/file_id.json', mode="x", encoding='utf-8')
        file.close()
    except JSONDecodeError:
        """Файл создан, но он пуст"""
        filenames = {}

    if len(filenames) > 2:
        await bot.send_message(message.chat.id, "Нельзя загружать на сервер более 3-х инструкций!")
    else:
        await bot.send_message(message.chat.id, "Загружаю файл на сервер...")
        response: bool = download_new_document(message, file_info)
        if response:
            await bot.send_message(message.chat.id, f"Файл {message.document.file_name} успешно загружен!")
        else:
            await bot.send_message(message.chat.id, "Ошибка загрузки!")

