import pyodbc
import os
from dotenv import load_dotenv

# crear una funcion que conecte a la bdd
def connect_db():
    load_dotenv()
    server = os.environ.get("server")
    database = os.environ.get("database")
    username = os.environ.get("username")
    password = os.environ.get("password")

    try:
        connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};PORT=1433"
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        return None
