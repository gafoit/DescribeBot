import logging
import os

from aiogram import Router, types
from aiogram import F
from Bot.keyborads.about_us import about_us_keyboard
from aiogram.utils.media_group import MediaGroupBuilder

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

contact_gft = "*Контакты Даниила*:\n\n" \
              "Почта: `daniilgafoit@gmail.com`\n" \
              "Телеграм: @First\_gafoit"
contact_Anny = "*Контакты Анны*:\n\n" \
               "Почта: `anna171613iq@gmail.com`\n" \
               "Телеграм: @Annettka\_5\_for\_love\_5"


@router.message(F.text == "©️ О нас")
async def about_us(message: types.Message):
    await message.delete()

    builder = MediaGroupBuilder()
    builder.add_photo(media=types.FSInputFile(os.getcwd() + "/Bot/assets/MyLoveAnny.jpg"))
    builder.add_photo(
        media=types.FSInputFile(os.getcwd() + "/Bot/assets/MyMe.jpg"),
        caption=about_us_text
    )

    await message.answer_media_group(
        media=builder.build()
    )

    await message.answer(back_text, parse_mode="HTML", reply_markup=about_us_keyboard())


@router.message(F.text == "Долбня Анна")
async def AnnyHandler(message: types.Message):
    await message.delete()
    await message.answer(contact_Anny, parse_mode="MarkdownV2", reply_markup=about_us_keyboard())


@router.message(F.text == "Ступников Даниил")
async def GftHandler(message: types.Message):
    await message.delete()
    await message.answer(contact_gft, parse_mode="MarkdownV2", reply_markup=about_us_keyboard())
