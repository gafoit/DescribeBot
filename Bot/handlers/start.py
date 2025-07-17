from aiogram import Router, types
from Bot.keyborads.main_menu import main_menu_keyboard
from aiogram import F

router = Router()

project_name = ('Разработке программной поддержки формирования и улучшения навыков ментальной арифметики и когнитивных '
                'процессов человека')
msg_text = f'Привет, я бот проекта по <blockquote>{project_name}</blockquote>'


@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer(msg_text, reply_markup=main_menu_keyboard(), parse_mode="HTML")
