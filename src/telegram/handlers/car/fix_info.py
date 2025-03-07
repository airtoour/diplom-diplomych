from typing import Any

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from db.models.cars.repository import CarsRepository
from telegram.keyboards.inline.inline import car_info
from telegram.states.update_car_info import UpdateCarInfo

from logger import logger


router = Router(name="fix_info")


@router.message(UpdateCarInfo.confirm_info)
async def confirm_car(message: Message, state: FSMContext, user: Any):
    try:
        await message.delete()

        if message.text == "Всё верно":
            await message.answer(
                "Я рад! 😊\n"
                "Если у Вас больше нет вопросов, связанных с машиной, "
                "то выберите, пожалуйста, интересующую Вас команду "
                "в меню команд слева снизу"
            )
        elif message.text == "Не верно":
            await message.answer(
                text="Оу, что именно не так в названии Вашей машины?\n"
                     "Выберите необходимую часть, в которой проблема ниже",
                reply_markup=car_info(user.id)
            )
        else:
            if message.text.startswith("/"):
                await message.answer("Окей, переключаемся...")
    except Exception as e:
        logger.error(f"Confirm Car: {e}")
        await message.answer(
            "Кажется, произошла какая-то ошибка.\n"
            "Стараемся разобраться с этим, извините за неудобства..."""
        )
    finally:
        await state.clear()


@router.callback_query(F.data.startswith("info:"))
async def problem_parts(callback: CallbackQuery, state: FSMContext):
    try:
        field = callback.data.split(":")[-1]

        await callback.message.edit_text(
            f"Очень жаль, что так получилось 😔\n"
            f"Давайте изменим эту часть для корректности.\n"
            f"Напишите ниже корректную информацию."
        )
        await state.set_state(UpdateCarInfo.correct_part)
        await state.update_data(problem_field=field)
    except Exception as e:
        logger.error(f"Problem Parts: {e}")
        await callback.answer(
            "Кажется, произошла какая-то ошибка.\n"
            "Стараемся разобраться с этим, извините за неудобства..."
        )


@router.message(UpdateCarInfo.correct_part)
async def update_part(message: Message, state: FSMContext, user: Any):
    try:
        problem_field = await state.get_value("problem_field")
        new_value = message.text

        await CarsRepository.update_car(user.id, problem_field, new_value)

        await message.edit_text(
            "Всё! Поправили. Надеюсь, такого больше не случится, успехов!"
        )
    except Exception as e:
        logger.error(f"Update Part: {e}")
        await message.answer(
            "Кажется, произошла какая-то ошибка.\n"
            "Стараемся разобраться с этим, извините за неудобства..."
        )
    finally:
        await state.clear()
