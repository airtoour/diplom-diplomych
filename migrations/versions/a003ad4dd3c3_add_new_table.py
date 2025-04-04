"""add new table

Revision ID: a003ad4dd3c3
Revises: 11c52083918d
Create Date: 2025-04-01 11:27:56.769271

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a003ad4dd3c3'
down_revision: Union[str, None] = '11c52083918d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carbon_footprints',
    sa.Column('id', sa.UUID(), nullable=False, comment='ID Записи следа'),
    sa.Column('car_id', sa.UUID(), nullable=False, comment='ID автомобиля'),
    sa.Column('actual', sa.Float(), nullable=False, comment='Текущее значение углеродного следа'),
    sa.Column('updated_at', sa.DateTime(), nullable=False, comment='Дата обновления'),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('cars', 'id',
               existing_type=sa.UUID(),
               comment='ID автомобиля',
               existing_nullable=False)
    op.alter_column('cars', 'user_id',
               existing_type=sa.UUID(),
               comment='ID владельца',
               existing_nullable=False)
    op.alter_column('cars', 'brand_name',
               existing_type=sa.VARCHAR(),
               comment='Марка',
               existing_nullable=False)
    op.alter_column('cars', 'model_name',
               existing_type=sa.VARCHAR(),
               comment='Модель',
               existing_nullable=False)
    op.alter_column('cars', 'gen_name',
               existing_type=sa.VARCHAR(),
               comment='Модификация',
               existing_nullable=False)
    op.alter_column('cars', 'year',
               existing_type=sa.INTEGER(),
               comment='Год выпуска',
               existing_nullable=False)
    op.alter_column('cars', 'mileage',
               existing_type=sa.INTEGER(),
               comment='Пробег',
               existing_nullable=False)
    op.alter_column('cars', 'full',
               existing_type=sa.VARCHAR(),
               comment='Полное название',
               existing_nullable=False)
    op.alter_column('users', 'id',
               existing_type=sa.UUID(),
               comment='ID пользователя',
               existing_nullable=False)
    op.alter_column('users', 'tg_user_id',
               existing_type=sa.BIGINT(),
               comment='TelegramID',
               existing_nullable=False)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               comment='Имя пользователя',
               existing_nullable=False)

    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    op.execute("""
        -- Создание временного набора данных (CTE)
        WITH fuel_data AS (
            SELECT uuid_generate_v4()                  AS id,
                   'АИ-80'                             AS fuel_type,
                   80                                  AS octane_number,
                   'Евро-4'                            AS quality_standard,
                   50                                  AS sulfur_content_ppm,
                   25.0                                AS aromatic_content_percent,
                   2.31                                AS co2_per_liter_combustion,
                   0.45                                AS co2_per_liter_production,
                   2.76                                AS total_carbon_footprint,
                   'Бензин низкого октана, чаще 
                   используется в сельской местности.' AS description
             UNION ALL
            SELECT 'АИ-92', 92, 'Евро-5', 10, 20.0, 2.35, 0.42, 2.77,
                   'Самый распространенный бензин в СНГ.'
             UNION ALL
            SELECT 'АИ-95', 95, 'Евро-5', 10, 18.0, 2.38, 0.40, 2.78,
                   'Премиальный бензин с улучшенными экологическими характеристиками.'
             UNION ALL
            SELECT 'АИ-98', 98, 'Евро-5', 10, 15.0, 2.40, 0.38, 2.78,
                   'Используется для высокофорсированных двигателей.'
             UNION ALL
            SELECT 'ДТ (Дизель)', 0, 'Евро-5', 10, NULL, 2.68, 0.50, 3.18,
                   'Для сравнения (дизельное топливо). Октановое число не применяется.'
        )

        -- Вставка данных из CTE в таблицу
        INSERT INTO gasoline_carbon_footprint (
            fuel_type,
            octane_number,
            quality_standard,
            sulfur_content_ppm,
            aromatic_content_percent,
            co2_per_liter_combustion,
            co2_per_liter_production,
            total_carbon_footprint,
            description
        )
        SELECT * FROM fuel_data
    """)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Имя пользователя',
               existing_nullable=False)
    op.alter_column('users', 'tg_user_id',
               existing_type=sa.BIGINT(),
               comment=None,
               existing_comment='TelegramID',
               existing_nullable=False)
    op.alter_column('users', 'id',
               existing_type=sa.UUID(),
               comment=None,
               existing_comment='ID пользователя',
               existing_nullable=False)
    op.alter_column('cars', 'full',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Полное название',
               existing_nullable=False)
    op.alter_column('cars', 'mileage',
               existing_type=sa.INTEGER(),
               comment=None,
               existing_comment='Пробег',
               existing_nullable=False)
    op.alter_column('cars', 'year',
               existing_type=sa.INTEGER(),
               comment=None,
               existing_comment='Год выпуска',
               existing_nullable=False)
    op.alter_column('cars', 'gen_name',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Модификация',
               existing_nullable=False)
    op.alter_column('cars', 'model_name',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Модель',
               existing_nullable=False)
    op.alter_column('cars', 'brand_name',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Марка',
               existing_nullable=False)
    op.alter_column('cars', 'user_id',
               existing_type=sa.UUID(),
               comment=None,
               existing_comment='ID владельца',
               existing_nullable=False)
    op.alter_column('cars', 'id',
               existing_type=sa.UUID(),
               comment=None,
               existing_comment='ID автомобиля',
               existing_nullable=False)
    op.drop_table('carbon_footprints')
    # ### end Alembic commands ###
