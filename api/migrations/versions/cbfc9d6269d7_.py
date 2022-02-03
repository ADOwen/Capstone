"""empty message

Revision ID: cbfc9d6269d7
Revises: 09f65e48471a
Create Date: 2022-02-03 14:38:01.800864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbfc9d6269d7'
down_revision = '09f65e48471a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cart_item_id_fkey', 'cart', type_='foreignkey')
    op.drop_column('cart', 'item_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('cart_item_id_fkey', 'cart', 'product', ['item_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###