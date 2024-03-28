from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramAPIError, AiogramError

from src.telegram.bot import dp
from src.db.config import session
from src.telegram.states import UserStates
from src.models import Users
from src.exceptions import server_exceptions
from src.telegram.keyboards.inline.inline import signup_tap_link


@dp.message(Command('support'))
async def support(message: Message, state: FSMContext):
    try:
        user = session.query(Users).filter_by(tg_user_id=message.from_user.id).first()

        if user:
            await message.answer('Если тебе понадобилась помощь, я постараюсь помочь тебе.\n'
                                 '\n'
                                 '\n'
                                 'Как стать частью нашей команды?\n'
                                 ''
                                 '\n'
                                 'Для вопросов по твоему заказу нажми на /order\n'
                                 'Там ты сможешь заказать:\n'
                                 '\n'
                                 '1. Необходимый товар для машины\n'
                                 '2. Проверить статус своего заказа\n'
                                 '\n')
        else:
            await message.answer('Сначала ты зарегистрируйся, а потом ты сможешь пользоваться нашей системой.')
    except Exception as e:
        print('SUPPORT: ', e)