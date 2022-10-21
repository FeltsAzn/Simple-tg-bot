from config import BOT_TOKEN
from telebot.async_telebot import AsyncTeleBot

"""Специальный отдельный питоновский файл,
 для связывания стартового файла и обработчиков"""

bot = AsyncTeleBot(BOT_TOKEN)

