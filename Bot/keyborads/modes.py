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
        [InlineKeyboardButton(text='🟠 Ментальная Арифметика',
                              url="https://telegra.ph/Rezhim-Formuly-dlya-mentalnoj-arifmetiki-07-20"),
         InlineKeyboardButton(text='🟠 Общий счёт', url="https://telegra.ph/Modul-Obshchij-schyot-07-20")],
        [InlineKeyboardButton(text="🟣 Концентрация", url="https://telegra.ph/Modul-Koncentraciya-07-20")],
        [InlineKeyboardButton(text="🟠 Найди пару", url="https://telegra.ph/Modul-Najdi-Paru-07-20"),
         InlineKeyboardButton(text="🟠 Шульте", url="https://telegra.ph/Modul-Tablica-SHulte-07-20")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
