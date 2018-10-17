"""empty message

Revision ID: 46f669e68155
Revises: 
Create Date: 2018-10-16 12:48:56.835043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46f669e68155'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('round',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=12), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trainer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=12), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('race',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('id_round', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_round'], ['round.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('snail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=12), nullable=False),
    sa.Column('trainer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('race_participants',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_snail', sa.Integer(), nullable=True),
    sa.Column('id_race', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_race'], ['race.id'], ),
    sa.ForeignKeyConstraint(['id_snail'], ['snail.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('race_result',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.Column('time_to_finish', sa.Integer(), nullable=False),
    sa.Column('did_not_finish', sa.Boolean(), nullable=False),
    sa.Column('id_race_participants', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_race_participants'], ['race_participants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('race_result')
    op.drop_table('race_participants')
    op.drop_table('snail')
    op.drop_table('race')
    op.drop_table('trainer')
    op.drop_table('round')
    # ### end Alembic commands ###
