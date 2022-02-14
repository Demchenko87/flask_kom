"""empty message

Revision ID: fd3d680a76ba
Revises: 8869c5942021
Create Date: 2022-01-31 10:41:24.019736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd3d680a76ba'
down_revision = '8869c5942021'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('about_us', 'title_seo')
    op.drop_column('about_us', 'desc_seo')
    op.drop_column('premium', 'title_seo')
    op.drop_column('premium', 'desc_seo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('premium', sa.Column('desc_seo', sa.TEXT(), nullable=True))
    op.add_column('premium', sa.Column('title_seo', sa.VARCHAR(length=160), nullable=True))
    op.add_column('about_us', sa.Column('desc_seo', sa.TEXT(), nullable=True))
    op.add_column('about_us', sa.Column('title_seo', sa.VARCHAR(length=160), nullable=True))
    # ### end Alembic commands ###
