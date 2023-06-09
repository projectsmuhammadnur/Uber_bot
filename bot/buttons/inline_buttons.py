from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def yes_or_no():
    design = [
        [InlineKeyboardButton(text="✅", callback_data="✅"), InlineKeyboardButton(text="❌", callback_data="❌")]
    ]
    imk = InlineKeyboardMarkup(inline_keyboard=design)
    return imk