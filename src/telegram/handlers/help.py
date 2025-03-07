from aiogram import Router, filters, types
from logger import logger


router = Router(name="help")


@router.message(filters.Command("help"))
async def help_command(message: types.Message):
    try:
        await message.delete()

        await message.answer(
            "📄 Список доступных команд:\n"
            "\n"
            "<b>1. /car</b>\n"
            "<blockquote>"
            "Команда, позволяющая зарегистрировать Вашу машину в нашей системе, "
            "чтобы помогать Вам было намного легче.\n"
            "Никаких конфиденциальных данных для нас не требуется, "
            "всего лишь название и год производства для нас достаточно."
            "</blockquote>"
            "\n"
            "<b>2. /solution</b>\n"
            "<blockquote>"
            "Команда, которая позволит подобрать необходимую запчасть для Вашей машины."
            "</blockquote>"
            "\n"
            "<b>3. /social</b>\n"
            "<blockquote>"
            "Команда, которая позволяет вывести ссылки на наши другие социальные сети, "
            "где много различной интересной информации.\n"
            "Там можно следить за новостями и новыми обновлениями."
            "</blockquote>"
        )
    except Exception as e:
        logger.error(f"Help: {e}")
        await message.answer(
            "Кажется, произошла какая-то ошибка.\n"
            "Стараемся разобраться с этим, извините за неудобства..."
        )
