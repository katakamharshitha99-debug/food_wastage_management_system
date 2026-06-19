import pyodbc

def get_connection():

    conn = pyodbc.connect(
        r"DRIVER={ODBC Driver 17 for SQL Server};"
        r"SERVER=SWEETY\SQLEXPRESS;"
        r"DATABASE=Food_wastage;"
        r"Trusted_Connection=yes;"
    )

    return conn
import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            r"DRIVER={ODBC Driver 17 for SQL Server};"
            r"SERVER=SWEETY\SQLEXPRESS;"
            r"DATABASE=Food_wastage;"
            r"Trusted_Connection=yes;"
        )
        return conn

    except Exception as e:
        print(f"Database Connection Error: {e}")
        return None