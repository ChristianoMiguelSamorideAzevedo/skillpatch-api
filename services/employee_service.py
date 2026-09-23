import sqlite3

from config import DATABASE_NAME


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def get_all_employees():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    connection.close()

    return employees

def create_employee(name, email, position):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO employees (name, email, position)
        VALUES (?, ?, ?)
        """,
        (name, email, position)
    )

    connection.commit()

    connection.close()
