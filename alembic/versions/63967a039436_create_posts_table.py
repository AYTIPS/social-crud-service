"""create posts table

Revision ID: 63967a039436
Revises: 
Create Date: 2025-09-17 14:00:11.504248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63967a039436'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table('posts')
    """Downgrade schema."""
    pass
