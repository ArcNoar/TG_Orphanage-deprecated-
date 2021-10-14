import logging

from aiogram import Dispatcher

#from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    bahus = 736557383
    Noah = 340981880
    try:
        #await dp.bot.send_message(bahus, "Очередной тестовый запуск.")
        await dp.bot.send_message(Noah, "АЛЕ БЛЯ, ЗАЕБАЛ")
    except Exception as err:
        logging.exception(err)
