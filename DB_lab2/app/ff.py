import time
import sys
import psycopg2
import pandas as pd
import csv


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

username = 'postgres'
password = 'PetroIsFucker55'
database = 'DB_lab_1'
# database = 'DB_lab_2'
host = 'db'
# host = 'localhost'
port = "5432"
# port = "5433"


df = pd.read_csv('Odata2020File.csv', encoding='windows-1251', delimiter=';')

# робимо список з типв клонок
column_types = get_columns_type(df)

# create table
column_names_str = ', '.join(df.columns.map(lambda x: f'"{x}"').tolist())
fields = df.columns

a=0
for i in range(5):
    print(df.iloc[i][0])
    print(df['outid'][i])

