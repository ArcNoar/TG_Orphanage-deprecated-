from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from loader import dp
from states.PhraseState import addphrases
import asyncio

from utils.data_base import sql_add_command

from aiogram.dispatcher.filters import Text

Noah = 340981880
user_id = None
@dp.message_handler(commands="ph_add", state=None)
async def pha_Start(message: types.Message):
    global user_id
    user_id = message.from_user.id
    if user_id == Noah:
        await addphrases.Category.set()
        await message.reply('Категория ?')
    else:
        await message.reply('Ты самозванец йобанный')

@dp.message_handler(state='*', commands = 'отмена')
@dp.message_handler(Text(equals='отмена', ignore_case = True),state='*')
async def cancel_handler(message: types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Оки оки, еще нахуй пойти можешь.')

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






