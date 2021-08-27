from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.SomeState import meanless
import asyncio

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await dp.bot.send_message(340981880, f'Тут чорт написал, его Айди : {user_id}')
    await dp.bot.send_message(340981880, f'Тут чорт написал, его сообщение : \n {message.text}')
    if message.text == 'Я состоятельный' and meanless.statecounter == 0:
        await message.answer('Похуй, будешь состоятельным хуем.')
        await meanless.kekstate.set()
        meanless.statecounter += 1
    elif message.text == 'Я состоятельный' and meanless.statecounter != 0:
        await message.answer('Нахуй иди, не состоятельный ты')   
    else:
        await message.answer(f"Ты не состоятельный Хуй."
                         f"Твой сблев:\n"
                         f"{message.text}")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer("Ты конечно теперь состоятельный хуй,но мне поебать.")
    await asyncio.sleep(3)
    await message.answer('А вообще пошел нахуй,я забираю твое состояние')
    user_id = message.from_user.id
    await dp.bot.send_message(340981880, f'Тут чорт написал, его Айди : {user_id}')
    await state.finish()
    
    

