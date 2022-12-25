"""empty message

Revision ID: 1d92b4ffd183
Revises: c8c1e25ae74e
Create Date: 2022-12-13 12:31:56.414833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d92b4ffd183'
down_revision = 'c8c1e25ae74e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.alter_column('summary',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.Text(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.alter_column('summary',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)

    # ### end Alembic commands ###