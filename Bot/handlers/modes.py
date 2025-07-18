from aiogram import Router, types
from aiogram import F
# from Bot.keyborads.modes import modes_keyboard
from Bot.keyborads.back import back_keyboard
from Bot.keyborads.modes import modes_keyboard, inline_modes_keyboard

router = Router()


@router.message(F.text == "🔡 Модули проекта")
async def mode_handler(message: types.Message):
    await message.answer('Статьи про модули приложений', reply_markup=inline_modes_keyboard())
    await message.answer('Выше можно перейти к статьям про модули приложения.', reply_markup=back_keyboard())
    await message.delete()


@router.message(F.text == "🟠 Ментальная Арифметика")
async def mental_math(msg: types.Message):
    await msg.answer(
        'Предлагаем ознакомиться со следующей статьёй о реализации данного модуля в нашем проекте:\n'
        ' <a href="https://telegra.ph/Mentalnaya-arifmetika-07-18">Статья по ментальной арифметике</a>',
        parse_mode='HTML')
