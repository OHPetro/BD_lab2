from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
import time
import sys
import psycopg2
import pandas as pd
import csv
pd.set_option('display.max_columns', None)

def get_columns_type(df):
    column_types = []
    for column in df.columns:
        column_type = df[column].dtype
        if column_type == 'int64':
            column_types.append(f"INTEGER")
        elif column_type == 'float64':
            column_types.append(f"FLOAT")
        else:
            column_types.append(f"TEXT")
    return column_types

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:PetroIsFucker55@localhost:5433/DB_lab_2'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

__all__ = ['app','db']


# if __name__ == '__main__':
#     app.run(debug=True)

# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     email = db.Column(db.Text, unique = True)
#
# class God(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     email = db.Column(db.Text, unique = True)
#
# class God2(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     email = db.Column(db.Text, unique = True)
#
# class User2(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.Text, unique = True)
#     email = db.Column(db.Text, unique = False)
#
# # antony = User1(name = 'Anton', email = 'gay')
#
# rows = []
# for i in range(10):
#
#     row = User2(name=f'Anton{i}', email='gay')
#     rows.append(row)
#
#
#
# with app.app_context():
#     db.create_all()
#     db.session.add_all(rows)
#     db.session.commit()
#     User2.query.all()



