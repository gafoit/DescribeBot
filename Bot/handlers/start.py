from aiogram import Router, types
from Bot.keyborads.main_menu import main_menu_keyboard
import logging
from aiogram import F

logging.basicConfig(level=logging.INFO)

router = Router()

project_name = ('Разработка программной поддержки формирования и улучшения навыков ментальной арифметики и когнитивных '
                'процессов человека')
msg_text = f'Привет, я бот проекта <blockquote>{project_name}</blockquote>\nНиже можете найти меню для поиска нужной информации о проекте'


@router.message(F.text.in_({"/start", "🔙 В Меню"}))
async def cmd_start(message: types.Message):
    msg_id = await message.answer_photo(types.FSInputFile("Bot/assets/Cool_mental_logo.png"), msg_text,
                                        reply_markup=main_menu_keyboard(), parse_mode="HTML")
    logging.info(msg_id.photo[-1].file_unique_id)
    logging.info(message.from_user.id)
