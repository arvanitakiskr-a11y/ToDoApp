"""Create phone number for user column

Revision ID: c021f96ff551
Revises: 
Create Date: 2026-08-08 22:40:25.027981

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c021f96ff551'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('Users', sa.Column('phone_number' , sa.String(),nullable = True))


def downgrade() -> None:
    op.drop_column('users','phone_number')
