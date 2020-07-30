"""empty message

Revision ID: e05941a0da74
Revises: 
Create Date: 2020-07-29 23:05:02.950469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e05941a0da74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('new_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first', sa.String(length=80), nullable=True),
    sa.Column('last', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('new_user')
    # ### end Alembic commands ###
