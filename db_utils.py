import sqlite3
import pandas as pd

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS oee_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id TEXT,
        location TEXT,
        date TEXT,
        operating_time REAL,
        planned_production_time REAL,
        good_count INTEGER,
        reject_count INTEGER,
        ideal_cycle_time REAL,
        oee REAL
    );
    """
    conn.execute(query)
    conn.commit()

def insert_data(conn, df):
    df.to_sql("oee_data", conn, if_exists="replace", index=False)

def query_data(conn, query):
    try:
        return pd.read_sql_query(query, conn)
    except Exception as e:
        print(f"Query failed: {e}")
        return pd.DataFrame()