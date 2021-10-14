from aiogram.dispatcher.filters.state import StatesGroup, State


class addphrases(StatesGroup):
    Category = State()
    Phrase = State()
    Answer = State()
    Rep_Influence = State()
    Rep_Immunity = State()