"""Add contact column to owner

Revision ID: 0b58e709c546
Revises: 6e97a233c897
Create Date: 2024-11-08 23:31:28.834058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b58e709c546'
down_revision = '6e97a233c897'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('owner', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contact', sa.String(length=20), nullable=True))

    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.alter_column('type',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.alter_column('type',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)

    with op.batch_alter_table('owner', schema=None) as batch_op:
        batch_op.drop_column('contact')

    # ### end Alembic commands ###
