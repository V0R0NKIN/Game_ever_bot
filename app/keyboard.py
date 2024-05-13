from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types

# Inline клавіатура
def progeckt():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text='Iнструменти', callback_data='_6'))
    builder.add(types.InlineKeyboardButton(text='Правила трох ігор', callback_data='_7'))
    return builder.as_markup()
def start():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text='🎮Ігри🕹️', callback_data='_4'))
    builder.add(types.InlineKeyboardButton(text='🎲Інструменти🏀', callback_data='_5'))
    return builder.as_markup()

def ruels():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text='Ігра UNO⏺', callback_data='_1'))
    builder.add(types.InlineKeyboardButton(text='Ігра в дурака♠️', callback_data='_2'))
    builder.add(types.InlineKeyboardButton(text='Ігра покер🃏', callback_data='_3'))
    return builder.as_markup()

def instrument():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text='🎲Кості🎲', callback_data='_8'))
    builder.add(types.InlineKeyboardButton(text='🪙Монетка🪙', callback_data='_9'))
    return builder.as_markup()


def ponel():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Monetka'))
    builder.add(types.KeyboardButton(text='Dice'))
    markeup = builder.as_markup()
    markeup.resize_keyboard = True
    return markeup