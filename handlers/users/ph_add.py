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
        await addphrases.Adding.set()
        await message.reply('Ввод в формате КАТЕГОРИЯ | ФРАЗА | ОТВЕТ | РЕПУТАЦИЯ (Каждый ввод должен начинать с новой строки)')
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

@dp.message_handler(state=addphrases.Adding)
async def ph_Category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Batch_of_phrase'] = message.text 
        extracted = tuple(data.values())[0] # Вытаскивает список из локальной памяти
        new_batch = extracted.split('\n') # Разделяет группы по спискам где разделитель новая строка
        
        list_of_triggers = [] # list [['Category','Phrase','Answer','Rep'],['Category2','Phrase2','Answer2','Rep2']]
        for elem in new_batch:
            new_trigger = elem.split('|') # Разбив строки списка на элементы
            list_of_triggers.append(new_trigger)
            
    await sql_add_command(list_of_triggers)
    await state.finish()








