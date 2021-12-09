from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

import asyncio
from time import sleep


# Общий хендлер
#340981880

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):  # TODO почистить и разбить этот хендлер
    if message.from_user.id == message.from_user.id :
        if message.text == 'Я состоятельный' :
            await message.answer('К сожалению я не могу определить вашего состояния')
        elif message.text == 'Ира сердечко':
            await message.answer('__000000___00000 \n _00000000_0000000 \n _0000000000000000 \n __00000000000000 \n ____00000000000 \n _______00000 \n _________0')
            await dp.bot.send_message(340981880, message.from_user.id)
            for i in range(228):
                await dp.bot.send_message(message.from_user.id, 'Ира')
        else:
            await dp.bot.send_message(340981880, message.from_user.id)
            await message.answer(f"Не поняла запроса\n"
                                 f"Ваше сообщение:\n"
                                 f"{message.text}")
    
    else:
        pass



# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.from_user.id == 340981880:
        await message.answer("Обнаружено неизвестное состояние. Возвращаю состояние к изначальному.")
        await state.finish()
    else:
        await dp.bot.send_message(340981880, message.from_user.id)
        await state.finish()
