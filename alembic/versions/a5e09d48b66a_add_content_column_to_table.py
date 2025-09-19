"""add content column to table

Revision ID: a5e09d48b66a
Revises: 63967a039436
Create Date: 2025-09-17 19:50:11.844120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5e09d48b66a'
down_revision: Union[str, Sequence[str], None] = '63967a039436'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content ')
    """Downgrade schema."""
    pass
