import os

from aiogram import Router, types
from aiogram import F
from Bot.keyborads.back import back_keyboard

router = Router()


def get_photo_url(user_id):
    data = []
    with open(os.getcwd() + "/Bot/handlers/about_project_pics.txt", 'r') as f:
        data = f.readlines()
    return data[user_id % len(data)]


@router.message(F.text == "ℹ️ О проекте")
async def about_project(message: types.Message):
    await message.delete()
    await message.answer_photo(
        photo=types.URLInputFile(get_photo_url(message.from_user.id)),
        caption="<b>О проекте</b>\n\n"
                "В мире цифровых технологий очень важно уметь обрабатывать гигантский объем информации, "
                "проходящий через нас ежедневно.\n\n"
                "Тем не менее, не каждый человек способен с этим справиться. "
                "Именно поэтому важно с детства развивать, а во взрослом возрасте поддерживать когнитивные процессы.\n\n"

                "<b>Данный проект разрабатывается именно с этой целью.</b>\n\n"

                "Как уже упоминалось, наш проект помогает развивать и поддерживать когнитивные навыки "
                "людей разных возрастов. Для этого мы используем различные методики, реализуя комплексный "
                "подход к проблеме и предлагая решения, подходящие многим людям.\n\n"

                "<b>Структура проекта:</b>\n"
                "• Разрабатываем Desktop-приложение\n"
                "• Создаем веб-платформу для взаимодействия\n\n"

                "Пользователи могут применять методики улучшения когнитивных процессов дома "
                "(например, для своих детей), а реабилитационные центры — собирать данные о работе с пациентами.\n\n"

                "В перспективе наше решение поможет улучшить память и концентрацию внимания, "
                "что и является главной целью разработки.",
        parse_mode="HTML", reply_markup=back_keyboard())
