from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.PhraseState import addphrases
import asyncio

from utils.data_base import sql_add_command


@dp.message_handler(commands="ph_add", state=None)
async def pha_Start(message: types.Message):
    await addphrases.Category.set()
    await message.reply('Категория ?')


@dp.message_handler(state=addphrases.Category)
async def ph_Category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Category'] = message.text
    await addphrases.next()
    await message.reply('Фраза ?')


@dp.message_handler(state=addphrases.Phrase)
async def ph_Phrase(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Phrase'] = message.text
    await addphrases.next()
    await message.reply('Ответ к фразе ?')


@dp.message_handler(state=addphrases.Answer)
async def ph_Answer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Answer'] = message.text
    await addphrases.next()
    await message.reply('Влияние на репутацию ?')


@dp.message_handler(state=addphrases.Rep_Influence)
async def ph_Influence(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Rep_Influence'] = int(message.text)
    
    await sql_add_command(state)
    await state.finish()


"""@dp.message_handler(state=addphrases.Rep_Immunity)
async def ph_Immunity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Rep_Immunity'] = message.text
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()"""



