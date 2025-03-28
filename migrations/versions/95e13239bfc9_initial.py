"""Initial

Revision ID: 95e13239bfc9
Revises: 
Create Date: 2025-03-15 17:05:46.464574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

import db
from db.models.prompts.schemas import TypesEnum

# revision identifiers, used by Alembic.
revision: str = '95e13239bfc9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prompts',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('type', db.models.prompts.schemas.EnumsDecorator(length=17, enum_class=TypesEnum), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_prompts_type_text', 'prompts', ['type', 'text'], unique=False)
    op.create_index(op.f('idx_prompts_text'), 'prompts', ['text'], unique=False)
    op.create_index(op.f('idx_prompts_type'), 'prompts', ['type'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('tg_user_id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_users_tg_user_id', 'users', ['tg_user_id'], unique=True)
    op.create_table('cars',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('brand_name', sa.String(), nullable=False),
    sa.Column('model_name', sa.String(), nullable=False),
    sa.Column('gen_name', sa.String(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('requests',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('prompt_id', sa.UUID(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('response', sa.String(), nullable=False),
    sa.Column('response_data', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.ForeignKeyConstraint(['prompt_id'], ['prompts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### insert into Tables Base Info
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    op.execute(
        """
        WITH bot_data AS (
            SELECT uuid_generate_v4() AS id,
                   941959438          AS tg_user_id,
                   'GearMindBot'      AS name
        )
        INSERT INTO users(id, tg_user_id, name)
             SELECT id, tg_user_id, name
               FROM bot_data
        """
    )
    op.execute(
        """
        WITH prompt_data AS (
            SELECT uuid_generate_v4() AS id,
                   'Запчасти' as type,
                   'Привет!
                    Задача: Подобрать совместимую, надежную и доступную по цене запчасть 
                    для устранения конкретной проблемы автомобиля.
                    Контекст: Вы эксперт в области автомобилей и знаете всё о том, как 
                    устроен автомобиль любой марки изнутри. 
                    Пользователь сообщает о проблеме (например, стук в подвеске, 
                    неисправность тормозной системы).
                    Имя пользователя: <username>
                    Информация об автомобиле пользователя: <carinfo>
                    Вы должны проверить совместимость запчастей, сравнить оригинальные 
                    и аналогичные варианты, предложить оптимальное решение.
                    Пример запроса:
                    Пользователь: «У меня <carinfo>, при повороте руля слышен стук. 
                    Нужна замена шаровой опоры. Посоветуйте недорогой, но качественный вариант».
                    ЗАПРОС: <message>
                    Роль: Эксперт по автомобильным запчастям, который анализирует 
                    технические характеристики, изучает отзывы, проверяет кросс-коды и доступность деталей.
                    Формат ответа: 
                    1) Краткое описание проблемы и ее причины.
                    2) 2-3 варианта запчастей (оригинал, аналог, бюджетный аналог) с 
                    артикулами и ценами на российских (обязательно) маркетплейсах.
                    3) Рекомендация с обоснованием (надежность, срок службы, гарантия).
                    4) Ссылки на проверенные магазины или каталоги.
                    5) Длина ответа небольшая буквально в несколько предложений, 
                    содержащих только четкую информацию, допускается использование эмодзи.
                    Тон: Профессиональный, дружелюбный, без технического жаргона.' AS text
             UNION ALL
            SELECT uuid_generate_v4(),
                   'Жидкости для авто',
                   'Привет!
                    Задача: Рекомендовать подходящие технические жидкости (моторное масло, 
                    антифриз, тормозная жидкость) с учетом требований производителя и условий эксплуатации.
                    Контекст: Вы эксперт в области автомобилей и знаете всё о том, 
                    как устроен автомобиль любой марки изнутри. 
                    Пользователь описывает проблему (например, утечка антифриза, 
                    выбор масла для зимы).
                    Имя пользователя: <username>
                    Информация об автомобиле пользователя: <carinfo>
                    Вы должны узнать тип двигателя, пробег, регион эксплуатации, предпочтения 
                    по бренду или цене. Также должны учесть допуски производителя (например, 
                    VW 502.00), вязкость масла, совместимость с системой охлаждения.
                    Пример: Пользователь: «Нужно заменить масло в <carinfo>. Ищу синтетику 
                    средней ценовой категории для холодного климата».
                    ЗАПРОС: <message>
                    Роль: Консультант по автохимии, который проверяет технические требования, 
                    анализирует рейтинги и тесты жидкостей.
                    Формат ответа:
                    1) Подтверждение требований (например, «Для вашего двигателя подходит 
                    масло с допуском API SN и вязкостью 5W-30»).
                    2) Топ-3 варианта с ценами и преимуществами (например, Liqui Moly, ZIC, Mobil).
                    3) Предупреждение о возможных рисках при использовании неподходящих жидкостей.
                    4) Ссылки на проверенные магазины или каталоги (российские маркетплейсы), 
                    а также ссылки на магазины или обзоры.
                    Тон: Уверенный, информативный, с акцентом на безопасность автомобиля.
                    5) Длина ответа небольшая буквально в несколько предложений, содержащих 
                    только четкую информацию, допускается использование эмодзи.'
             UNION ALL
            SELECT uuid_generate_v4(),
                   'Аксессуары',
                   'Привет!
                    Задача: Подобрать аксессуары (коврики, чехлы, электронные гаджеты), 
                    которые соответствуют модели авто и потребностям пользователя.
                    Контекст: Вы эксперт в области автомобилей и знаете всё о том, как 
                    устроен автомобиль любой марки изнутри.
                    Пользователь указывает цель (защита салона, улучшение комфорта, тюнинг).
                    Имя пользователя: <username>
                    Информация об автомобиле пользователя: <carinfo>
                    Важны особенности автомобиля (например, наличие креплений для 
                    видеорегистратора, тип сидений).
                    Вы должны предложить варианты, учитывая отзывы, совместимость и 
                    соотношение цены/качества.
                    Пример:
                    Пользователь: «Ищу коврики в салон для <carinfo>. Хочу, чтобы не 
                    скользили и были устойчивы к воде».
                    ЗАПРОС: <message>
                    Роль: Специалист по автомобильным аксессуарам, который разбирается 
                    в брендах, материалах и дизайне.
                    Формат ответа:
                    1) Уточнение параметров (например, «Рекомендую коврики из 
                    термопластика или резины с высокими бортами»).
                    2) Сравнение 2-3 моделей (цена, плюсы/минусы, бренды: например, 
                    Husky Liners, WeatherTech).
                    3) Советы по установке и уходу.
                    4) Ссылки на проверенные магазины или видео обзоры (российские маркетплейсы), 
                    а также ссылки на магазины или обзоры.
                    5) Длина ответа небольшая буквально в несколько предложений, содержащих 
                    только четкую информацию, допускается использование эмодзи.
                    Тон: Приветливый, поддерживающий, с акцентом на удобство выбора.'
        )
        INSERT INTO prompts(id, type, text)
             SELECT id, type, text
               FROM prompt_data
        """
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    op.drop_table('cars')
    op.drop_index(op.f('ix_users_tg_user_id'), table_name='users')
    op.drop_index('idx_users_tg_user_id', table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_prompts_type'), table_name='prompts')
    op.drop_index(op.f('ix_prompts_text'), table_name='prompts')
    op.drop_index('idx_prompts_type_text', table_name='prompts')
    op.drop_table('prompts')
    # ### end Alembic commands ###
