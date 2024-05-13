import random
from asyncio import sleep

from aiogram import Bot, Dispatcher, F, Router, exceptions, types
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from app.keyboard import start
from aiogram.fsm.context import FSMContext
from app.tool.tool_viselnitsa import GameStepsForm


# Усі обробники варто закріплювати за Router або Dispatcher
router = Router()

death_man = {
    1:'''
      |  
      0  
    ''',
    2:'''
      |
      0
      |
    ''',
    3:'''
      |
      0
     /| 
    ''',
    4:'''
      |
      0
     /|\\
    ''',
    5:'''
      |
      0
     /|\\
     / \\
    ''',

}


def get_random_word():
    wordlist = ['мандарин', 'яблоко', 'груша', 'виноград', 'апельсин', 'манго']
    return random.choice(wordlist)


def leter_in_word(word, letter, dashes_word) -> str:
    indexes = []
    for i, char in enumerate(word):
        if char == letter:
            indexes.append(i)

    dashes_word = list(dashes_word)
    for i in indexes:
        dashes_word[i] = letter

    return ''.join(dashes_word)


@router.callback_query(F.data == "_4")
async def game_visel_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Ігра Вісельница")
    await callback.message.answer('Привіт! Добро пожалувати у гру Висельница')
    await callback.message.answer('Вгадай фрукт')
    await callback.answer()

    await state.set_state(GameStepsForm.process_game)

    word = get_random_word()
    dashes_word = "_" * len(word)

    await state.update_data(word=word, dash_word=dashes_word, turns=0)

    await callback.message.answer(f"Слово: {dashes_word}")
    await callback.message.answer("Нaзви букву\n")


@router.message(GameStepsForm.process_game, F.text.len() == 1)
async def game_vissel_process(message: Message, state: FSMContext):
    letter = message.text
    data_game = await state.get_data()

    new_dash_word = leter_in_word(data_game["word"], letter, data_game["dash_word"])

    await state.update_data(dash_word=new_dash_word)

    if "_" not in new_dash_word:
        await message.answer(new_dash_word)
        await message.answer("Ти виграв🙂")
        await state.set_state(GameStepsForm.end_game)
        await state.clear()

    elif data_game["turns"] == 5:
        await message.answer(new_dash_word)
        await message.answer("Ти програв😢")
        await state.set_state(GameStepsForm.end_game)
        await state.clear()

    elif letter in data_game["word"]:
        if data_game["turns"] > 5 or "_" in new_dash_word:
            await message.answer("Вгадав\n")
            await message.answer(new_dash_word)
            await message.answer("Нaзви наступну букву\n")
        elif data_game["turns"] == 5:
            await message.answer("Вгадав\n")
            await message.answer(new_dash_word)

    else:
        data_game = await state.update_data(turns=data_game["turns"] + 1)
        await message.answer("Нe вгадав\n")
        await message.answer(new_dash_word)
        await message.answer(death_man[data_game["turns"]])


@router.message(GameStepsForm.end_game)
async def game_vissel_end(message: Message, state: FSMContext):
    data_game = await state.get_data()

    print(data_game)
    await state.clear()