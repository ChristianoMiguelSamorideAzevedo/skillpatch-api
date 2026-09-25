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

    employees_list = []

    for employee in employees:

        employees_list.append({
            "id": employee[0],
            "name": employee[1],
            "email": employee[2],
            "position": employee[3]
        })

    return employees_list


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


def get_employee_by_id(employee_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()

    connection.close()

    if employee is None:
        return None

    return {
        "id": employee[0],
        "name": employee[1],
        "email": employee[2],
        "position": employee[3]
    }


def delete_employee(employee_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    connection.commit()

    connection.close()
