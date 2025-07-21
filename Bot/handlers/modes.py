from aiogram import Router, types
from aiogram import F

from Bot.keyborads.back import back_keyboard
from Bot.keyborads.modes import inline_modes_keyboard

router = Router()


@router.message(F.text == "🔡 Модули проекта")
async def mode_handler(message: types.Message):
    await message.delete()
    await message.answer('Статьи про модули приложений', reply_markup=inline_modes_keyboard())
    await message.answer('Выше можно перейти к статьям про модули приложения.', reply_markup=back_keyboard())
