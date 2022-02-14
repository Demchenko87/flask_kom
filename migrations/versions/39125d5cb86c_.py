"""empty message

Revision ID: 39125d5cb86c
Revises: f2e0daa2e794
Create Date: 2022-02-08 18:52:45.488692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39125d5cb86c'
down_revision = 'f2e0daa2e794'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('divorced',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=160), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=160), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.Column('divorced_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['divorced_id'], ['divorced.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    op.drop_table('divorced')
    # ### end Alembic commands ###