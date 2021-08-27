from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("На, только отъебись уже: ",
            "/start - Пользуешься правами бога? Пидор ебаный.",
            "/help - Не жди здесь помощи.")

    await message.answer("\n".join(text))
