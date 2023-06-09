import json
import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.buttons.reply_buttons import back_button, keys_buttons_poschitat, keys_buttons
from bot.dispatcher import dp, bot


@dp.message_handler(Text("отмена"), state='*')
async def back_handler(msg: types.Message, state: FSMContext):
    await state.set_state('keys')
    await msg.answer(text="Bo`limlardan birini tanlang⬇️", reply_markup=keys_buttons())


@dp.message_handler(Text("Uber"), state='keys')
async def uber_handler(msg: types.Message, state: FSMContext):
    await state.set_state("uber_file")
    await msg.answer(text="информация текст+фото", reply_markup=back_button())


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state="uber_file")
async def uber_file_handler(msg: types.Message, state: FSMContext):
    if msg.document.mime_type == 'text/csv':
        file = await bot.download_file_by_id(file_id=msg.document.file_id)
        file_name = msg.document.file_name
        file_path = os.path.join('Uber_files', file_name)
        with open(file_path, 'wb') as new_file:
            new_file.write(file.getvalue())
            await state.set_state("keys")
        await msg.answer(text="CSV File saqlandi", reply_markup=keys_buttons_poschitat())
        with open("paths.json", 'r') as data_file:
            data = json.load(data_file)
        with open("paths.json", 'w') as data_file:
            data[0].append(f"Uber_Bot/Uber_files/{msg.document.file_name}")
            json.dump(data, data_file, indent=4)
    else:
        await state.set_state("uber_file")
        await msg.answer(text="информация текст+фото", reply_markup=back_button())


@dp.message_handler(Text("Bolt"), state='keys')
async def uber_handler(msg: types.Message, state: FSMContext):
    await state.set_state("bolt_file")
    await msg.answer(text="информация текст+фото", reply_markup=back_button())


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state="bolt_file")
async def uber_file_handler(msg: types.Message, state: FSMContext):
    if msg.document.mime_type == 'text/csv':
        file = await bot.download_file_by_id(file_id=msg.document.file_id)
        file_name = msg.document.file_name
        file_path = os.path.join('Bolt_files', file_name)
        with open(file_path, 'wb') as new_file:
            new_file.write(file.getvalue())
            await state.set_state("keys")
        await msg.answer(text="CSV File saqlandi", reply_markup=keys_buttons_poschitat())
        with open("paths.json", 'r') as data_file:
            data = json.load(data_file)
        with open("paths.json", 'w') as data_file:
            data[0].append(f"Uber_Bot/Bolt_files/{msg.document.file_name}")
            json.dump(data, data_file, indent=4)
    else:
        await state.set_state("bolt_file")
        await msg.answer(text="информация текст+фото", reply_markup=back_button())


@dp.message_handler(Text("FreeNow"), state='keys')
async def uber_handler(msg: types.Message, state: FSMContext):
    await state.set_state("freenow_file")
    await msg.answer(text="информация текст+фото", reply_markup=back_button())


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state="freenow_file")
async def uber_file_handler(msg: types.Message, state: FSMContext):
    if msg.document.mime_type == 'application/pdf':
        file = await bot.download_file_by_id(file_id=msg.document.file_id)
        file_path = f"Freenow_files/{msg.document.file_name}"
        with open(file_path, "wb") as new_file:
            new_file.write(file.getvalue())
            await state.set_state("keys")
        await msg.answer(text="PDF File saqlandi", reply_markup=keys_buttons_poschitat())
        with open("paths.json", 'r') as data_file:
            data = json.load(data_file)
        with open("paths.json", 'w') as data_file:
            data[0].append(f"Uber_Bot/Freenow_files/{msg.document.file_name}")
            json.dump(data, data_file, indent=4)
    else:
        await state.set_state("freenow_file")
        await msg.answer(text="информация текст+фото", reply_markup=back_button())