import sqlite3
import pandas as pd
from pathlib import Path


def init_db():
    Path("output").mkdir(exist_ok=True)
    conn = sqlite3.connect("output/marketing_data.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes_api (
        id INTEGER PRIMARY KEY,
        Nombre TEXT,
        Apellido TEXT,
        email TEXT,
        company TEXT,
        city TEXT,
        username TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS posts_api (
        userId INTEGER,
        id INTEGER PRIMARY KEY,
        title TEXT,
        body TEXT
    )
    """)

    conn.commit()
    conn.close()


def load_csv_to_db():
    conn = sqlite3.connect("output/marketing_data.db")

    df_users = pd.read_csv("output/clientes_api.csv")
    df_posts = pd.read_csv("output/posts_api.csv")

    # Asegurarse que userId esté bien escrito (por si pandas lo cambió)
    if 'userId' not in df_posts.columns:
        print("Error: 'userId' no está en el archivo posts_api.csv")
        print("Columnas encontradas:", df_posts.columns)
        return

    df_users.to_sql("clientes_api", conn, if_exists="replace", index=False)
    df_posts.to_sql("posts_api", conn, if_exists="replace", index=False)
    conn.close()


def run_queries():
    conn = sqlite3.connect("output/marketing_data.db")
    cur = conn.cursor()

    print("\nUsuarios ordenados por ciudad:")
    for row in cur.execute("SELECT * FROM clientes_api ORDER BY city"):
        print(row)

    print("\nCantidad de posts por usuario:")
    query = """
    SELECT c.username, COUNT(p.id) as cantidad_posts
    FROM clientes_api c
    JOIN posts_api p ON c.id = p.userId
    GROUP BY c.username
    ORDER BY cantidad_posts DESC
    """
    for row in cur.execute(query):
        print(row)

    conn.close()
