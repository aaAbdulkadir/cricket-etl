import sqlite3
import pandas as pd

cleaned_data_path = 'data/cleaned_scraped_data.csv'
transformed_data_path = 'data/transformed_data.csv'
db_name = 'cricket.db'

def make_connection(db_name):
    return sqlite3.connect(db_name)

def load_data(filepath):
    return pd.read_csv(filepath, index_col=0)

def send_to_sqlite(df, table_name):
    conn = make_connection(db_name)
    df.to_sql(table_name, con=conn)
    conn.close()

def load():
    send_to_sqlite(load_data(cleaned_data_path), 'raw_data')
    send_to_sqlite(load_data(transformed_data_path), 'totals')
    print('Data loaded to sqlite db.')

"""RUN SCRIPT"""
load()