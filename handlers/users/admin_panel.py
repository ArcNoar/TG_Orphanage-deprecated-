from aiogram import types
from aiogram.dispatcher import FSMContext
import sys
from loader import dp
from states.PhraseState import addphrases
import asyncio


@dp.message_handler(commands="shutdown", state=None)
async def pha_Start(message: types.Message):
    user_id = message.from_user.id
    if user_id == 340981880:
        await message.reply('А? Спать пора? Ну вот попутной всем дороги нахуй.')
        sys.exit()
        
    else:
        await message.reply('Ты самозванец, нахуй пошел.')