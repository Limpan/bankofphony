"""Basic model.

Revision ID: e442fd8d7b7f
Revises: 
Create Date: 2017-04-20 20:01:45.273873

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'e442fd8d7b7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('funds',
    sa.Column('id', sa.String(length=4), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('risk', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=254), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('registered_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('last_seen', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=8), nullable=True),
    sa.Column('balance', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_accounts_number'), 'accounts', ['number'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_accounts_number'), table_name='accounts')
    op.drop_table('accounts')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('funds')
    # ### end Alembic commands ###