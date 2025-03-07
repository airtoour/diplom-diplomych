from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from telegram.keyboards.inline.inline import social_links

from loguru import logger


router = Router(name="social")


@router.message(Command("social"))
async def social(message: Message):
    try:
        await message.delete()

        await message.answer(
            text="Хочешь узнать лучше о нас?\n"
                 "Переходи по ссылкам на социальные сети ниже!\n"
                 "\n"
                 "Подписавшись, ты сможешь получать самую актуальную "
                 "информацию и следить за обновлениями нашего сервиса 🫶\n"
                 "\n\n"
                 "<blockquote>"
                 "<i>* - Признана экстремистской соц. сетью на территории РФ</i>"
                 "</blockquote>",
            reply_markup=social_links
        )
    except Exception as e:
        logger.exception("social", e)
