import sqlite3

from config import DATABASE_NAME


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            position TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Banco de dados criado com sucesso!")


create_database()
