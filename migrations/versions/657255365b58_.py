"""empty message

Revision ID: 657255365b58
Revises: 72c41941b129
Create Date: 2021-12-06 19:02:02.208380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '657255365b58'
down_revision = '72c41941b129'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    # ### end Alembic commands ###