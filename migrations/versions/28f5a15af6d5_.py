"""empty message

Revision ID: 28f5a15af6d5
Revises: be4d3c523539
Create Date: 2022-02-22 14:46:06.067353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f5a15af6d5'
down_revision = 'be4d3c523539'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.String(length=160), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###
