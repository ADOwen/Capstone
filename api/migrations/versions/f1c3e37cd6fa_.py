"""empty message

Revision ID: f1c3e37cd6fa
Revises: 7efb7e250c72
Create Date: 2022-01-23 19:28:05.629169

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f1c3e37cd6fa'
down_revision = '7efb7e250c72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=200), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('post', sa.Column('text', sa.Text(), nullable=False))
    op.alter_column('post', 'date_created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_constraint('post_title_key', 'post', type_='unique')
    op.drop_constraint('post_user_id_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('post', 'image')
    op.drop_column('post', 'content')
    op.drop_column('post', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
    op.add_column('post', sa.Column('content', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('image', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key('post_user_id_fkey', 'post', 'user', ['user_id'], ['id'])
    op.create_unique_constraint('post_title_key', 'post', ['title'])
    op.alter_column('post', 'date_created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('post', 'text')
    op.drop_table('like')
    op.drop_table('comment')
    # ### end Alembic commands ###
