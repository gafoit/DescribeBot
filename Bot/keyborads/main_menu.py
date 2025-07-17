from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard():
    buttons = [
        [KeyboardButton(text="ℹ️ О проекте")],
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
