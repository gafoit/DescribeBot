from aiogram import Router, types
from aiogram import F
from Bot.keyborads.back import back_keyboard

router = Router()

about_us_text = 'Текст раздела "О нас"'


@router.message(F.text == "©️ О нас")
async def about_us(message: types.Message):
    await message.answer(about_us_text, reply_markup=back_keyboard())
