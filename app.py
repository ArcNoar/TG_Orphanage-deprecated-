from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

from utils.data_base import sql_start


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    
    # Дб по идее
    sql_start()

# Это мусорный код с прикрученной дб, но она никак не работает в самом тг, так что да, считай мусор

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates= True)
    