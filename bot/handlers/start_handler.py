from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.buttons.reply_buttons import main_menu_button
from bot.dispatcher import dp


@dp.message_handler(Text("главное меню"), state='*')
async def back_handler(msg: types.Message, state: FSMContext):
    await msg.answer(text=f"{msg.from_user.first_name} asosiy menudasiz🏠", reply_markup=main_menu_button())
    await state.finish()


@dp.message_handler(commands='start')
async def start_handler(msg: types.Message):
    await msg.answer(text=f"Assalomu aleykum {msg.from_user.first_name}👋\n\nBo`limlardan birini tanlang⬇️", reply_markup=main_menu_button())