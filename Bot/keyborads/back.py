from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def back_keyboard():
    buttons = [
        [KeyboardButton(text="🔙 В Меню")],

    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)