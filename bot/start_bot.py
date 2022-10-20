from heandlers import *
import asyncio
import logging


def start():
    asyncio.run(bot.infinity_polling(skip_pending=True,
                                     logger_level=logging.DEBUG,
                                     timeout=5))


if __name__ == '__main__':
    try:
        start()
    except Exception as ex:
        with open('logs.txt', 'a') as file:
            file.write(f'{ex}\n')
        start()
