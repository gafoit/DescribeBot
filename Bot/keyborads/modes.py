from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# color_circles = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "⚫", "⚪", "🟤"]


def modes_keyboard():
    buttons = [
        [KeyboardButton(text='<a href="https://telegra.ph/Mentalnaya-arifmetika-07-18">🟠 Ментальная Арифметика</a>'),
         KeyboardButton(text="🟠 Общий счёт")],
        [KeyboardButton(text="🟣 Концентрация")],
        [KeyboardButton(text="🟠 Найди пару"), KeyboardButton(text="🟠 Шульте")],
        [KeyboardButton(text="🔙 В Меню")],
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder="Воспользуйтесь меню:")
