"""create table

Revision ID: bbbeee2e6408
Revises: d535e23e190a
Create Date: 2025-09-09 14:50:13.499778

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bbbeee2e6408'
down_revision: Union[str, Sequence[str], None] = 'd535e23e190a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
