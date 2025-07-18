from aiogram import Router, types
from aiogram import F
from Bot.keyborads.modes import modes_keyboard

router = Router()

text = 'Раздел модулей приложения. Выберите интересующий чтобы узнать больше.'


@router.message(F.text == "🔡 Модули проекта")
async def mode_handler(message: types.Message):
    await message.answer(text, reply_markup=modes_keyboard())


@router.message(F.text == "🟠 Ментальная Арифметика")
async def mental_math(msg: types.Message):
    await msg.answer('<a href="https://telegra.ph/Mentalnaya-arifmetika-07-18">', parse_mode='HTML')
