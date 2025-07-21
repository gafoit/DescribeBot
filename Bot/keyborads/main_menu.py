from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard():
    buttons = [
        [KeyboardButton(text="🔡 Модули проекта")],
        [KeyboardButton(text="ℹ️ О проекте"), KeyboardButton(text="©️ О нас")],
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
