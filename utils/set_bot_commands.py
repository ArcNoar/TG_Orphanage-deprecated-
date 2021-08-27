from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Нахуй иди, я не хочу работать."),
            types.BotCommand("help", "В другом месте ищи помощи."),
        ]
    )
