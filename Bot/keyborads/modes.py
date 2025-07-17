from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# color_circles = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "⚫", "⚪", "🟤"]


def modes_keyboard():
    buttons = [
        [KeyboardButton(text="🟠 Ментальная Арифметика")],
        [KeyboardButton(text="🟣 Общий счёт")],
        [KeyboardButton(text="🟠 Концентрация")],
        [KeyboardButton(text="🟣 Найди пару")],
        [KeyboardButton(text="🟠 Шульте")],
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
