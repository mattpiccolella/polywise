"""Adding file association

Revision ID: f2ee73d17a0c
Revises: d9073a7afbb7
Create Date: 2024-01-27 09:45:29.821040

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2ee73d17a0c'
down_revision: Union[str, None] = 'd9073a7afbb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversation_document',
    sa.Column('conversation_id', sa.Integer(), nullable=False),
    sa.Column('document_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversation.id'], ),
    sa.ForeignKeyConstraint(['document_id'], ['document.id'], ),
    sa.PrimaryKeyConstraint('conversation_id', 'document_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('conversation_document')
    # ### end Alembic commands ###
