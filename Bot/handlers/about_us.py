import logging
import os

from aiogram import Router, types
from aiogram import F
from aiogram.utils import media_group
from Bot.keyborads.about_us import inline_about_us_keyboard
from Bot.keyborads.back import back_keyboard

router = Router()
logging.basicConfig(level=logging.INFO)

about_us_text = "О нас.\n\n" \
                "<b>Глава проекта</b>\n" \
                "<i>Долбня Анна Панагиотисовна</i>\n" \
                'Студентка 4 курса КемГУ по направлению "Прикладная математика и информатика".\n' \
                "Идейный вдохновитель проекта.\n\n" \
                "<b>Программист проекта</b>\n" \
                "<i>Ступников Даниил Игоревич</i>\n" \
                'Студент 4 курса КемГУ по направлению "Прикладная математика и информатика".\n' \
                "Главный программист проекта во всех направлениях, от Desktop-приложений до Telegram-ботов и Web-программирования\n\n"
back_text = "Ниже можно найти наши контакты для связи."


@router.message(F.text == "©️ О нас")
async def about_us(message: types.Message):
    await message.answer_media_group(
        media_group.MediaGroupBuilder(
            [types.InputMediaPhoto(media=types.FSInputFile(os.getcwd() + "/Bot/assets/MyLoveAnny.jpg")),
             types.InputMediaPhoto(media=types.FSInputFile(os.getcwd() + "/Bot/assets/MyMe.jpg"))],
            caption=about_us_text).build())
    await message.answer(back_text, parse_mode="HTML", reply_markup=inline_about_us_keyboard())
    msg = await message.answer("Техническое сообщение. Если вы это видели, развидьте", reply_markup=back_keyboard())
    await msg.delete()
    await message.delete()


@router.callback_query(F.data.startswith("Anny"))
async def AnnyHandler(message: types.Message):
    logging.info('Callback работает')
