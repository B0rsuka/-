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
     # ������� ������
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
    # ������� ������ ��� �����.
    map_str = ""
    # �������� �� ���� ���������
    for y in range(rows * 2 - 1):
        # �������� �� ���� �����������
        for x in range(cols * 2 - 1):
            # ���� ������� ������ � map_cell �������� True, �����.
            if map_cell[x + y * (cols * 2 - 1)]:
                # ��������� ������.
                map_str += "??"
                # ���� ���������� ��������� � ������������ ������, �����.
            elif (x, y) == player:
                # �� ������ �������� ������.
                map_str += "?"
                # ��� (�� ���� ��������� �������.)
            else:
                # ��������� ������.
                map_str += "??"
                # ��������� ������� ������ � map_cell, ����� ����������� �� ���� �����������.
        map_str += "\n"
    # ���������� ��, ��� ����������, � �����.
    return map_str

@dp.message(Command("play"))
async def cmd_start(message: types.Message):
     # c������ ��������
     map_cell = get_map_cell(cols, rows)
     # �������� id ����
     Chat_id = message.get_chat().id
     # �������� ���������� � ��������� � ��� �� ���������
     user_data = {
          'map': map_cell,
          'x': 0,
          'y': 0
     }
     # ������ ���������� � ����� �������
     maps[Chat_id] = user_data
     await message.answer( get_map_str(map_cell, (0, 0)), reply_markup=get_keyboard())