from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

import asyncio
from time import sleep

from states.Conver_State import Regular_Conver

# Общий хендлер


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):  # TODO почистить и разбить этот хендлер
    
    if message.text == 'Я состоятельный' :
        await message.answer('Много хочешь чел')
    elif message.text == 'Режим Беседы.':
        await Regular_Conver.conversation.set()
        await message.answer('А?')
    else:
        await message.answer(f"Ты не состоятельный Хуй."
                             f"Твой сблев:\n"
                             f"{message.text}")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer("Схуяли у тебя есть состояние?")
    await asyncio.sleep(2)
    await message.answer('А пошел нахуй,я забираю твое состояние')
    await state.finish()
