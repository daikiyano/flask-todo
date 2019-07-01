"""empty message

Revision ID: 2ae38acad8dc
Revises: 75a1c5688eb9
Create Date: 2019-07-01 11:00:17.351796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ae38acad8dc'
down_revision = '75a1c5688eb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('test', sa.VARCHAR(length=140), nullable=True))
    # ### end Alembic commands ###
