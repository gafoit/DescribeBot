from aiogram import Router, types
from Bot.keyborads.main_menu import main_menu_keyboard

router = Router()


@router.message()
async def cmd_start(message: types.Message):
    await message.answer(
        "К сожалению, я не знаю такого. Используйте кнопки для управления или команду /start",
        reply_markup=main_menu_keyboard(), parse_mode="HTML")
