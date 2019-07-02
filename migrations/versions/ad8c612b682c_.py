"""empty message

Revision ID: ad8c612b682c
Revises: 
Create Date: 2019-07-02 19:50:17.326233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad8c612b682c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_image', sa.Text(), nullable=False),
    sa.Column('email', sa.String(length=140), nullable=True),
    sa.Column('username', sa.String(length=140), nullable=True),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('event', sa.Text(), nullable=True),
    sa.Column('facebook', sa.String(length=140), nullable=True),
    sa.Column('twitter', sa.String(length=140), nullable=True),
    sa.Column('instagram', sa.String(length=140), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('url', sa.String(length=140), nullable=True),
    sa.Column('university', sa.Integer(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.Column('email_confirmation_sent_on', sa.DateTime(), nullable=True),
    sa.Column('email_confirmed', sa.Boolean(), nullable=True),
    sa.Column('email_confirmed_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_image', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=False),
    sa.Column('event_date', sa.DateTime(), nullable=True),
    sa.Column('event_time', sa.Time(), nullable=True),
    sa.Column('organizer', sa.String(length=140), nullable=False),
    sa.Column('place', sa.String(length=140), nullable=False),
    sa.Column('entry', sa.Text(), nullable=False),
    sa.Column('way', sa.Text(), nullable=False),
    sa.Column('cost', sa.String(length=140), nullable=False),
    sa.Column('contact', sa.String(length=140), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['blog_post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['blog_post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_like')
    op.drop_table('comment')
    op.drop_table('followers')
    op.drop_table('blog_post')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
