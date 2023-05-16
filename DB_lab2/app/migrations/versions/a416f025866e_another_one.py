"""Another one

Revision ID: a416f025866e
Revises: 3224d4a6ae9a
Create Date: 2023-05-15 20:55:18.563676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a416f025866e'
down_revision = '3224d4a6ae9a'
branch_labels = None
depends_on = None


from app import app, db

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    class Students(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        birth = db.Column(db.Integer, unique=False)
        sextype = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        areaname = db.Column(db.Text, unique=False)
        tername = db.Column(db.Text, unique=False)
        regtypename = db.Column(db.Text, unique=False)
        tertypename = db.Column(db.Text, unique=False)
        classprofilename = db.Column(db.Text, unique=False)
        classlangname = db.Column(db.Text, unique=False)

    db.create_all()
    db.session.commit()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('name', name='user_name_key')
    )
    op.create_table('user1',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user1_pkey'),
    sa.UniqueConstraint('email', name='user1_email_key'),
    sa.UniqueConstraint('name', name='user1_name_key')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key')
    )
    op.create_table('god',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='god_pkey'),
    sa.UniqueConstraint('email', name='god_email_key')
    )
    op.create_table('user2',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user2_pkey'),
    sa.UniqueConstraint('name', name='user2_name_key')
    )
    op.create_table('god2',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='god2_pkey'),
    sa.UniqueConstraint('email', name='god2_email_key')
    )
    # ### end Alembic commands ###
