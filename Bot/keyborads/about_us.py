from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def about_us_keyboard():
    buttons = [
        [KeyboardButton(text="Долбня Анна"), KeyboardButton(text="Ступников Даниил")],
        [KeyboardButton(text="🔙 В Меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
