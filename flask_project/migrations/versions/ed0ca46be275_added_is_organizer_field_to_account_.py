"""Added is_organizer field to Account model

Revision ID: ed0ca46be275
Revises: d8bdb9ffa2cf
Create Date: 2024-12-03 18:33:18.192493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed0ca46be275'
down_revision = 'd8bdb9ffa2cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_organizer', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.drop_column('is_organizer')

    # ### end Alembic commands ###
