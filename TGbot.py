import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from cod import get_map_cell

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5993524543:AAGWT0Ql05FPZL8Xtuduee4bwNN4S7NcCw0")
dp = Dispatcher()

cols, rows = 8, 8
maps = {}

def get_keyboard():
     # создаем кнопки
    buttons = [
        [
            types.InlineKeyboardButton(text='?', callback_data='up',),
        ],
        [
            types.InlineKeyboardButton(text='?', callback_data='left',),
            types.InlineKeyboardButton(text='?', callback_data='right'),
        ],
        [
            types.InlineKeyboardButton(text='?', callback_data='down', ),
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def get_map_str(map_cell, player):
    # создаем строку дл€ карты.
    map_str = ""
    # проходим по всей вертикали
    for y in range(rows * 2 - 1):
        # проходим по всей горизонтали
        for x in range(cols * 2 - 1):
            # если текуща€ €чейка в map_cell €вл€етс€ True, тогда.
            if map_cell[x + y * (cols * 2 - 1)]:
                # добавл€ем символ.
                map_str += "??"
                # если координаты совпадают с координатами игрока, тогда.
            elif (x, y) == player:
                # мы должны добавить символ.
                map_str += "?"
                # или (во всех остальных случа€х.)
            else:
                # добавл€ем символ.
                map_str += "??"
                # добавл€ем перенос строки в map_cell, после прохождени€ по всей горизонтали.
        map_str += "\n"
    # возвращаем то, что получилось, в карту.
    return map_str

@dp.message(Command("play"))
async def cmd_start(message: types.Message):
     # cоздаем лаберинт
     map_cell = get_map_cell(cols, rows)
     # получ€ем id ч€та
     Chat_id = message.get_chat().id
     # содержет информацыю о лаберинте и где он находитс€
     user_data = {
          'map': map_cell,
          'x': 0,
          'y': 0
     }
     # додаем информацыю в общий словарь
     maps[Chat_id] = user_data
     await message.answer( get_map_str(map_cell, (0, 0)), reply_markup=get_keyboard())