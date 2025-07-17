from aiogram import Router, types
from Bot.keyborads.main_menu import main_menu_keyboard
from aiogram import F
router = Router()


@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Выберите режим:", reply_markup=main_menu_keyboard())
