from aiogram.filters import Command
import random
from asyncio import sleep
from aiogram import Bot, Dispatcher, exceptions, types
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from app.keyboard import instrument, start, progeckt, ponel, ruels
from aiogram.enums.dice_emoji import DiceEmoji

# Усі обробники варто закріплювати за Router або Dispatcher
router = Router()
@router.message(Command('infa'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт {message.from_user.full_name}!\nЦей бот🗿 Зроблен завдяки мові програмування Python💻\nв онлайн школі GoIteens.\n🫵Тобі потрібна додаткова інформація\nтоді заходь на їх сайт\n силка тут👉 https://goiteens.com/course/design/\nДякую за увагу")

#============================================================

# Обробник для команди /start
@router.message(Command('start'))
async def command_my_keyboard0(message: Message):
    await message.answer(text=f"Привіт {message.from_user.full_name} \nДавай почнемо✔️", reply_markup=ponel())
    await message.answer(text="Це всі наші розділи", reply_markup=start())

# Команда кости
@router.message(F.text == "Dice")
async def Dice(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)

# Монетка
@router.message(F.text == "Monetka")
async def Monetka  (message: Message):
    many = ["🎇Орёл🎇", "🎆Решка🎆"]
    random_many = random.choice(many)
    await message.answer(f"Випало {random_many}")

# Інструменти
@router.callback_query(F.data == "_5")
async def my_keyboard5(callback: CallbackQuery):
        await callback.message.answer("🎲Інструменти для\nнастільних ігор🏀", reply_markup=progeckt())
        await callback.answer()

# Команда для інструментов
@router.callback_query(F.data == "_6")
async def my_keyboard7(callback: CallbackQuery):
    await callback.message.answer(text="🎲Інструменти🏀", reply_markup=instrument())
    await callback.answer()

@router.callback_query(F.data == "_8")
async def my_keyboard8(callback: CallbackQuery) -> None:
    await callback.message.answer_dice(emoji=DiceEmoji.DICE)
    await callback.answer()

@router.callback_query(F.data == "_9")
async def my_keyboard9(callback: CallbackQuery):
    many = ["Орёл🪙", "Решка🪙"]
    random_many = random.choice(many)
    await callback.message.answer(f"Випало {random_many}")
    await callback.answer()


#Правила трьох ігор
@router.callback_query(F.data == "_7")
async def my_keyboard7(callback: CallbackQuery):
    await callback.message.answer(text="Правила трьох ігор", reply_markup=ruels())
    await callback.answer()
@router.callback_query(F.data == "_1")
async def my_keyboard1(callback: CallbackQuery):
    await callback.message.answer("Правила ігри UNO⏺:\nhttps://www.youtube.com/watch?v=6VzWiOi7R4U")
    await callback.answer()
@router.callback_query(F.data == "_2")
async def my_keyboard2(callback: CallbackQuery):
    await callback.message.answer("Правила ігри в дурака♠️:\nhttps://www.youtube.com/watch?v=qk67UHo6IlE")
    await callback.answer()
@router.callback_query(F.data == "_3")
async def my_keyboard3(callback: CallbackQuery):
    await callback.message.answer("Правила ігри покер🃏:\nhttps://www.youtube.com/watch?v=JLAi4XxF6dk")
    await callback.answer()
