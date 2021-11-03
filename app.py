from aiogram import executor

from loader import dp
import handlers # middlewars
from utils.notify_admins import on_startup_notify


from Ai_package.Contextual_AI.Contextual_DB import sql_start


async def on_startup(dispatcher):
    
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    # Дб по идее
    sql_start()




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates= False)
    