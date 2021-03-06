"""empty message

Revision ID: ffaecc16e7f8
Revises: 7557e6893083
Create Date: 2022-02-03 14:26:26.006773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffaecc16e7f8'
down_revision = '7557e6893083'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('cart_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product', 'cart', ['cart_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'cart_id')
    # ### end Alembic commands ###
