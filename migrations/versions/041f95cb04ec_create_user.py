"""create user

Revision ID: 041f95cb04ec
Revises: 
Create Date: 2022-01-24 20:18:47.447856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '041f95cb04ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(25)),
        sa.Column('password', sa.String(25))
    )


def downgrade():
    op.drop_table('user')
