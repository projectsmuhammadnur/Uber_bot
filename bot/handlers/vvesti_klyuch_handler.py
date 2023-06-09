import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.buttons.reply_buttons import back_menu_button, keys_buttons, main_menu_button
from bot.dispatcher import dp


@dp.message_handler(Text("ввести ключ"))
async def vvesti_klyuch_handler(msg: types.Message, state: FSMContext):
    await state.set_state("send_key")
    await msg.answer(text="введите ключ, который вам дали: ", reply_markup=back_menu_button())


@dp.message_handler(state='send_key')
async def check_key_handler(msg: types.Message, state: FSMContext):
    with open("keys.json", 'r') as file:
        data = json.load(file)
    for i in data:
        for j in i:
            if j == msg.text:
                async with state.proxy() as data:
                    data['key'] = msg.text
                await state.set_state("keys")
                await msg.answer(text="Bo`limlardan birini tanlang⬇️", reply_markup=keys_buttons())
                return
    await msg.answer(text="не активный ключ", reply_markup=main_menu_button())
    await state.finish()
