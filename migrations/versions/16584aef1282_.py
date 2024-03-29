"""empty message

Revision ID: 16584aef1282
Revises: 28f5a15af6d5
Create Date: 2022-02-22 14:50:45.604109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16584aef1282'
down_revision = '28f5a15af6d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.VARCHAR(length=160), nullable=True))
    # ### end Alembic commands ###
