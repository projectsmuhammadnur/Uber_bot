import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.buttons.inline_buttons import yes_or_no
from bot.buttons.reply_buttons import back_button, main_menu_button, keys_buttons_poschitat
from bot.dispatcher import dp, bot


@dp.message_handler(Text("отмена"), state=['wr', 'yes_or_no_vat', 'count', 'yes_or_no_count'])
async def back_handler(msg: types.Message, state: FSMContext):
    await state.set_state('delete_keys')
    await msg.answer(text="Bo`limlardan birini tanlang⬇️", reply_markup=keys_buttons_poschitat())


@dp.message_handler(Text("посчитать"), state='keys')
async def count_handler(msg: types.Message, state: FSMContext):
    await state.set_state("wr")
    await msg.answer(text="внесите такой процент VAT в снятие", reply_markup=back_button())


@dp.message_handler(state='wr')
async def count_yes_or_no_handler(msg: types.Message, state: FSMContext):
    number = None
    try:
        number = float(msg.text)
    except ValueError:
        pass
    if number is not None:
        await state.set_state("wr")
        await msg.answer(text="внесите такой процент VAT в снятие", reply_markup=back_button())
    else:
        await state.set_state("yes_or_no_vat")
        await msg.answer(text="введний VAT правильный?", reply_markup=yes_or_no())


@dp.callback_query_handler(state="yes_or_no_vat")
async def vat_yes_or_no_handler(call: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    if call.data == "✅":
        await state.set_state("count")
        await call.message.answer(text="введите сумму свои камисси", reply_markup=back_button())
    else:
        await state.set_state("wr")
        await call.message.answer(text="внесите такой процент VAT в снятие", reply_markup=back_button())


@dp.message_handler(state="count")
async def count_handler(msg: types.Message, state: FSMContext):
    number = None
    try:
        number = float(msg.text)
    except ValueError:
        pass
    if number is not None:
        await state.set_state("count")
        await msg.answer(text="введите сумму свои камисси", reply_markup=back_button())
    else:
        await state.set_state("yes_or_no_count")
        await msg.answer(text="комиссия введения правильная?", reply_markup=yes_or_no())


@dp.callback_query_handler(state="yes_or_no_count")
async def vat_yes_or_no_handler(call: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    if call.data == "✅":
        await call.message.answer(text="Key o`chirildi", reply_markup=main_menu_button())
        with open("keys.json", "r") as file:
            data = json.load(file)
        async with state.proxy() as state_data:
            pass
        for i in data:
            for j in i:
                if j == state_data['key']:
                    i.remove(j)
        with open("keys.json", "w") as file:
            json.dump(data, file, indent=4)
        await state.finish()
    else:
        await state.set_state("count")
        await call.message.answer(text="введите сумму свои камисси", reply_markup=back_button())
