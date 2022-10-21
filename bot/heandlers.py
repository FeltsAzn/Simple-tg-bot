from file_handler import get_file_id, download_new_document, check_file_repository
from loader import bot
from config import ADMIN_ID, ADMIN_NAME
import telebot


commads_for_bot = ["Товар 1", "Товар 2", "Товар 3", "Связаться с поддержкой"]


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
           f'По какому товару хотите получить инструкцию?'
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
    """Обработчик для выдачи контактов поддержки"""
    text = f"https://t.me/{ADMIN_NAME}"
    await bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text not in commads_for_bot, content_types=['text'])
async def invalid_command(message):
    """Обработчик случайного текста от пользователей"""
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
    filenames = check_file_repository()
    if len(filenames) > 2:
        await bot.send_message(message.chat.id, "Нельзя загружать на сервер более 3-х инструкций!")
    else:
        await bot.send_message(message.chat.id, "Загружаю файл на сервер...")
        response: bool = download_new_document(message, file_info)
        if response:
            await bot.send_message(message.chat.id, f"Файл {message.document.file_name} успешно загружен!")
        else:
            await bot.send_message(message.chat.id, "Ошибка загрузки!")

