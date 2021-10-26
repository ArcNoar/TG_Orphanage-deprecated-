from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
import asyncio

from states.Conver_State import Regular_Conver

#from utils.data_base import sql_responder


""" Это Хендлер для обычного беседного режима """

@dp.message_handler(state=Regular_Conver.conversation)
async def bot_echo(message: types.Message, state = FSMContext):
    if message.text == 'Закончим Беседу.':
        await message.answer('Оки Доки')
        await state.finish()
    else:
        #await sql_responder(message)
        pass
    
