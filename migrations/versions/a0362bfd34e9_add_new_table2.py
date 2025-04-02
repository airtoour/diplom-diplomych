"""add new table2

Revision ID: a0362bfd34e9
Revises: a003ad4dd3c3
Create Date: 2025-04-01 12:16:06.068803

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0362bfd34e9'
down_revision: Union[str, None] = 'a003ad4dd3c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carbon_gasoline',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('fuel_type', sa.String(), nullable=False, comment='Тип бензина'),
    sa.Column('octane_number', sa.Integer(), nullable=False, comment='Октановое число'),
    sa.Column('quality_standard', sa.String(length=20), nullable=False, comment='Стандарт (Евро-4, Евро-5 и т.п.)'),
    sa.Column('sulfur_content_ppm', sa.Integer(), nullable=False, comment='Содержание серы (ppm)'),
    sa.Column('aromatic_content_percent', sa.Float(), nullable=False, comment='Доля ароматических углеводородов (%)'),
    sa.Column('co2_per_liter_combustion', sa.Float(), nullable=False, comment='Выбросы CO₂ при сгорании (кг/л)'),
    sa.Column('co2_per_liter_production', sa.Float(), nullable=False, comment='Углеродный след производства (кг/л)'),
    sa.Column('total_carbon_footprint', sa.Float(), nullable=False, comment='Общий углеродный след (кг/л)'),
    sa.Column('description', sa.Text(), nullable=True, comment='Примечание'),
    sa.Column('last_updated', sa.DateTime(), nullable=False, comment='Дата обновления'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carbon_gasoline')
    # ### end Alembic commands ###
