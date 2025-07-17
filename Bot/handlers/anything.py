from aiogram import Router, types
from Bot.keyborads.back import back_keyboard

router = Router()


@router.message()
async def cmd_start(message: types.Message):
    await message.answer(
        "К сожалению, я не знаю такого. Используйте кнопки для управления или команду /start",
        reply_markup=back_keyboard(), parse_mode="HTML")
