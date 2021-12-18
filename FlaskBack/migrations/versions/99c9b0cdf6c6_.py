"""empty message

Revision ID: 99c9b0cdf6c6
Revises: 
Create Date: 2021-09-13 22:35:15.977838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99c9b0cdf6c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('airplanes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('income', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_airplanes_id'), 'airplanes', ['id'], unique=False)
    op.create_table('fleet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('income', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fleet_id'), 'fleet', ['id'], unique=False)
    op.create_table('infantry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('income', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_infantry_id'), 'infantry', ['id'], unique=False)
    op.create_table('medals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medal_type', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_medals_id'), 'medals', ['id'], unique=False)
    op.create_table('tanks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('income', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tanks_id'), 'tanks', ['id'], unique=False)
    op.create_table('army',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('infantry_id', sa.Integer(), nullable=True),
    sa.Column('tanks_id', sa.Integer(), nullable=True),
    sa.Column('airplanes_id', sa.Integer(), nullable=True),
    sa.Column('fleet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['airplanes_id'], ['airplanes.id'], ),
    sa.ForeignKeyConstraint(['fleet_id'], ['fleet.id'], ),
    sa.ForeignKeyConstraint(['infantry_id'], ['infantry.id'], ),
    sa.ForeignKeyConstraint(['tanks_id'], ['tanks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_army_id'), 'army', ['id'], unique=False)
    op.create_table('army_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('army_id', sa.Integer(), nullable=True),
    sa.Column('info', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['army_id'], ['army.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_army_info_id'), 'army_info', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_admin', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('army_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['army_id'], ['army.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('achievement_manager',
    sa.Column('medal_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['medal_id'], ['medals.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('medal_id', 'user_id')
    )
    op.create_index(op.f('ix_achievement_manager_user_id'), 'achievement_manager', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_achievement_manager_user_id'), table_name='achievement_manager')
    op.drop_table('achievement_manager')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_army_info_id'), table_name='army_info')
    op.drop_table('army_info')
    op.drop_index(op.f('ix_army_id'), table_name='army')
    op.drop_table('army')
    op.drop_index(op.f('ix_tanks_id'), table_name='tanks')
    op.drop_table('tanks')
    op.drop_index(op.f('ix_medals_id'), table_name='medals')
    op.drop_table('medals')
    op.drop_index(op.f('ix_infantry_id'), table_name='infantry')
    op.drop_table('infantry')
    op.drop_index(op.f('ix_fleet_id'), table_name='fleet')
    op.drop_table('fleet')
    op.drop_index(op.f('ix_airplanes_id'), table_name='airplanes')
    op.drop_table('airplanes')
    # ### end Alembic commands ###
