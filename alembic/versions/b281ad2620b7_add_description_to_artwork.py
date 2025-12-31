"""Add description to artwork

Revision ID: b281ad2620b7
Revises: 030d52158663
Create Date: 2025-12-30 21:42:13.623371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b281ad2620b7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('artworks', sa.Column('description', sa.String(), nullable=True))

def downgrade() -> None:
    op.drop_column('artworks', 'description')