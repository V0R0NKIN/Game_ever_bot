from aiogram.fsm.state import State, StatesGroup


class GameStepsForm(StatesGroup):
    process_game = State()
    end_game = State()

    word = ''
    dash_word = ''
    turns = 1