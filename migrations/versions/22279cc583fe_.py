"""empty message

Revision ID: 22279cc583fe
Revises: 9bf44bf2b4b2
Create Date: 2020-10-15 18:05:29.508857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22279cc583fe'
down_revision = '9bf44bf2b4b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'active')
    # ### end Alembic commands ###
