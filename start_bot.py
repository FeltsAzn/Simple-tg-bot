from loader import bot
from heandlers import *
from telebot import util
import asyncio



if __name__ == '__main__':
    # bot.infinity_polling(skip_pending=True)
    asyncio.run(bot.polling(allowed_updates=util.update_types, none_stop=True, skip_pending=True))
