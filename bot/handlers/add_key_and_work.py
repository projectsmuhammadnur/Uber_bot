import random

from aiogram import types
from aiogram.dispatcher.filters import Text
import json

from bot.buttons.reply_buttons import main_menu_button
from bot.dispatcher import dp


@dp.message_handler(Text("получить ключ"))
async def add_key(msg: types.Message):
    son = random.randint(99999, 999999)
    with open("keys.json", 'r') as f:
        data = json.load(f)
    data[0].append(str(son))
    with open("keys.json", 'w') as file:
        json.dump(data, file, indent=4)
    await msg.answer(text=f"Sizning keyingiz: {son}", reply_markup=main_menu_button())


@dp.message_handler(Text("как это работает?"))
async def add_key(msg: types.Message):
    await msg.answer(text="Kak eto rabotaet bosildi")