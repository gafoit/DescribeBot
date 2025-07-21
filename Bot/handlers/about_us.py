import os

from aiogram import Router, types
from aiogram import F
from aiogram.utils import media_group
from Bot.keyborads.back import back_keyboard

router = Router()

about_us_text = """
О нас.

"""


@router.message(F.text == "©️ О нас")
async def about_us(message: types.Message):
    await message.answer_media_group(media_group.MediaGroupBuilder(
        [types.InputMediaPhoto(media=types.FSInputFile(os.getcwd() + "/Bot/assets/MyLoveAnny.jpg")),
         types.InputMediaPhoto(media=types.FSInputFile(os.getcwd() + "/Bot/assets/MyMe.jpg"))],
        caption=about_us_text
    ).build())
    # await message.answer(about_us_text, reply_markup=back_keyboard())
