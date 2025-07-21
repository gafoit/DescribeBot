from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_about_us_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Долбня Анна", callback_data="Anny"),
         InlineKeyboardButton(text="Ступников Даниил", callback_data="gft")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
