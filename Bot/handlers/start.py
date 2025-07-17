from aiogram import Router, types
from Bot.keyborads.main_menu import main_menu_keyboard
from aiogram import F

router = Router()

project_name = ('Разработка программной поддержки формирования и улучшения навыков ментальной арифметики и когнитивных '
                'процессов человека')
msg_text = f'Привет, я бот проекта <blockquote>{project_name}</blockquote>'


@router.message(F.text in ["/start", "🔙 В Меню"])
async def cmd_start(message: types.Message):
    await message.answer(msg_text, reply_markup=main_menu_keyboard(), parse_mode="HTML")
