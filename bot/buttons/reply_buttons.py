from aiogram.types import ReplyKeyboardMarkup


def main_menu_button():
    rmk = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    rmk.add("получить ключ", "ввести ключ", 'как это работает?')
    return rmk


def keys_buttons_poschitat():
    rmk = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    rmk.add("Uber", "Bolt", "FreeNow", "посчитать")
    return rmk


def keys_buttons():
    rmk = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    rmk.add("Uber", "Bolt", "FreeNow")
    return rmk


def back_menu_button():
    rmk = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    rmk.add("главное меню")
    return rmk


def back_button():
    rmk = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    rmk.add("отмена")
    return rmk