from bot.loader import bot
from bot.heandlers import *
from telebot import util
import asyncio
import logging


def start():
    asyncio.run(bot.infinity_polling(skip_pending=True, logger_level=logging.DEBUG))


if __name__ == '__main__':
    # bot.infinity_polling(skip_pending=True)
    try:
        start()
    except Exception as ex:
        with open('logs.txt', 'a') as file:
            file.write(f'{ex}\n')
        start()
