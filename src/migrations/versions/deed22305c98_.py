"""empty message

Revision ID: deed22305c98
Revises: 86208497183b
Create Date: 2022-05-09 17:30:28.260040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'deed22305c98'
down_revision = '86208497183b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Crypto',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('Name', sa.String(), nullable=True),
    sa.Column('Symbol', sa.String(), nullable=True),
    sa.Column('Price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_table('Investor',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('firstName', sa.String(), nullable=True),
    sa.Column('lastName', sa.String(), nullable=True),
    sa.Column('userEmail', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('riskLevel', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('userEmail')
    )
    op.create_table('Stock',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('Name', sa.String(), nullable=True),
    sa.Column('Symbol', sa.String(), nullable=True),
    sa.Column('Price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_table('Stock and Crypto by risk',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('symbol', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('risk', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_table('Watchlist',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('userEmail', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('symbol', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['userEmail'], ['Investor.userEmail'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Watchlist')
    op.drop_table('Stock and Crypto by risk')
    op.drop_table('Stock')
    op.drop_table('Investor')
    op.drop_table('Crypto')
    # ### end Alembic commands ###