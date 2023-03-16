"""cascade

Revision ID: 3cecf2d1d863
Revises: 4e0726c4014c
Create Date: 2023-03-16 21:26:26.273086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cecf2d1d863'
down_revision = '4e0726c4014c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint('mahasiswa_ibfk_2', type_='foreignkey')
        batch_op.drop_constraint('mahasiswa_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_satu'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_dua'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('mahasiswa_ibfk_1', 'dosen', ['dosen_dua'], ['id'])
        batch_op.create_foreign_key('mahasiswa_ibfk_2', 'dosen', ['dosen_satu'], ['id'])

    # ### end Alembic commands ###