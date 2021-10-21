from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

import asyncio
from time import sleep


@dp.message_handler(state=None)
async def msg_log(message: types.Message):  # TODO почистить и разбить этот хендлер
    user_id = message.from_user.id

    if user_id == 340981880:
        pass
    else:
        
        await dp.bot.send_message(340981880, f'Тут чорт написал, его Айди : {user_id}')
        await dp.bot.send_message(340981880, f'Тут чорт написал, его сообщение : \n {message.text}')



@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def anti_state(message: types.Message, state: FSMContext):
    await message.answer("Схуяли у тебя есть состояние?")
    await asyncio.sleep(3)
    await message.answer('А пошел нахуй,я забираю твое состояние')
    user_id = message.from_user.id
    if user_id == 340981880:
        pass
    else:
        await dp.bot.send_message(340981880, f'Тут чорт написал, его Айди : {user_id}')
        await dp.bot.send_message(340981880, f'Тут чорт написал, его сообщение : \n {message.text}')
    await state.finish()