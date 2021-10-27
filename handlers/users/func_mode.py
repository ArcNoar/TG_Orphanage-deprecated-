from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

import asyncio
from time import sleep

from Ai_package.Contextual_AI.train import training
from states.Func_State import Func_State

# Admin Check
Noah = 340981880
user_id = None
# Функциональный  хендлер


@dp.message_handler(commands="func_mode", state=None)
async def func_start(message: types.Message):  
    global user_id
    user_id = message.from_user.id
    if user_id == Noah:
        await Func_State.func.set()
        await message.answer('А, ты по делу, оки оки.')

    else:
        await message.answer('Ты че ебанутый? Кыш отсюда')


@dp.message_handler(state=Func_State.func)
async def func_work(message: types.Message, state: FSMContext):
    if message.text == 'Обучить Ядро':
        await message.answer('О, нихуя себе. Ща сделаем')
        training()
        await dp.bot.send_message(message.from_user.id, 'Готово')
    elif message.text == 'Гуляй':
        await message.answer('Ага, нахуй иди')
        await state.finish()
    else:
        await message.answer(f"Дядь, ты че на старости лет совсем ебанулся?"
                             f"Нет такой команды:\n"
                             f"{message.text}")


"""
# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer("Схуяли у тебя есть состояние? У нас так не принято, я забираю его.")
    await state.reset_state()
"""