from aiogram import Router, types
from aiogram import F
from Bot.keyborads.modes import modes_keyboard

router = Router()

about_us_text = 'Раздел модулей приложения. Выберите интересующий чтобы узнать больше.'


@router.message(F.text == "🪜 Модули проекта")
async def mode_handler(message: types.Message):
    await message.answer(about_us_text, reply_markup=modes_keyboard())
