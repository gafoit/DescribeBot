from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# color_circles = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "⚫", "⚪", "🟤"]


def modes_keyboard():
    buttons = [
        [KeyboardButton(text='🟠 Ментальная Арифметика'),
         KeyboardButton(text="🟠 Общий счёт")],
        [KeyboardButton(text="🟣 Концентрация")],
        [KeyboardButton(text="🟠 Найди пару"), KeyboardButton(text="🟠 Шульте")],
        [KeyboardButton(text="🔙 В Меню")],
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder="Воспользуйтесь меню:")


def inline_modes_keyboard():
    buttons = [
        [InlineKeyboardButton(text='🟠 Ментальная Арифметика', url="https://telegra.ph/Mentalnaya-arifmetika-07-18"),
         InlineKeyboardButton(text="🟠 Общий счёт")],
        [InlineKeyboardButton(text="🟣 Концентрация")],
        [InlineKeyboardButton(text="🟠 Найди пару"), InlineKeyboardButton(text="🟠 Шульте")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
