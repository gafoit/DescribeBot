from aiogram import Router, types
from aiogram import F
router = Router()

@router.message(F.text == "ℹ️ О проекте")
async def info_command(message: types.Message):
    await message.answer("Это Telegram-бот для описания проекта. Используйте меню ниже.")
