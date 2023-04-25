from src.etl.load import *

def test_len_of_tables():
    conn = make_connection(db_name)
    cursor = conn.cursor()
    query = """ SELECT * FROM sqlite_master WHERE type='table' """
    cursor.execute(query)
    tables = cursor.fetchall()
    conn.close()
    assert len(tables) == 2

def test_row_raw():
    conn = make_connection(db_name)
    cursor = conn.cursor()
    query = """ SELECT NAME FROM raw_data LIMIT 1 """
    cursor.execute(query)
    name = cursor.fetchall()
    conn.close()
    assert name == [('Devon Conway',)]

def test_row_totals():
    conn = make_connection(db_name)
    cursor = conn.cursor()
    query = """ SELECT NAME FROM totals LIMIT 1 """
    cursor.execute(query)
    name = cursor.fetchall()
    conn.close()
    assert name == [('Faf du Plessis',)]


