"""Another 5

Revision ID: 403b7563bcbf
Revises: a20f4befc7a4
Create Date: 2023-05-16 11:48:53.257307

"""
from alembic import op
import sqlalchemy as sa
from app import app, db

# revision identifiers, used by Alembic.
revision = '403b7563bcbf'
down_revision = 'a20f4befc7a4'
branch_labels = None
depends_on = None


def upgrade():
    class Ukr(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Hist(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Math(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Phys(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Chem(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Bio(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Geo(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Engl(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Fra(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Deut(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    class Spa(db.Model):
        student_id = db.Column(db.Integer, primary_key=True)
        nametest = db.Column(db.Text, unique=False)
        teststatus = db.Column(db.Text, unique=False)
        ball100 = db.Column(db.Text, unique=False)
        ball12 = db.Column(db.Text, unique=False)
        ball = db.Column(db.Text, unique=False)
        adaptscale = db.Column(db.Text, unique=False)
        ptname = db.Column(db.Text, unique=False)
        regname = db.Column(db.Text, unique=False)
        ptareaname = db.Column(db.Text, unique=False)
        pttername = db.Column(db.Text, unique=False)

    db.create_all()
    db.session.commit()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('birth', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sextype', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('regname', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('areaname', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('tername', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('regtypename', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('tertypename', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('classprofilename', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('classlangname', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='students_pkey')
    )
    op.create_table('school',
    sa.Column('school_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('eoname', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('eotypename', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('eoregname', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('eoareaname', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('eotername', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('eoparent', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('school_id', name='school_pkey')
    )
    # ### end Alembic commands ###
