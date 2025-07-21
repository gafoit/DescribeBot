from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def inline_about_us_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Долбня Анна", callback_data="Anny"),
         InlineKeyboardButton(text="Ступников Даниил", callback_data="gft")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def about_us_keyboard():
    buttons = [
        [KeyboardButton(text="Долбня Анна"), KeyboardButton(text="Ступников Даниил")],
        [KeyboardButton(text="🔙 В Меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons)
