from flask import jsonify, request
from flask_openapi3 import OpenAPI

from services.employee_service import (
    get_all_employees,
    get_employee_by_id,
    delete_employee,
    create_employee
)

app = OpenAPI(__name__)

@app.route("/")
def home():
    return "SkillPatch API is running!"


@app.route("/employees", methods=["GET"])
def get_employees():

    employees = get_all_employees()

    return jsonify(employees)


@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):

    employee = get_employee_by_id(employee_id)

    return jsonify(employee)

@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee_route(employee_id):

    delete_employee(employee_id)

    return jsonify({
        "message": f"Employee {employee_id} deleted successfully"
    })


@app.route("/employees", methods=["POST"])
def create_employee_route():

    data = request.get_json()

    create_employee(
        data["name"],
        data["email"],
        data["position"]
    )

    return jsonify({
        "message": "Employee created successfully"
    }), 201


if __name__ == "__main__":
    app.run(debug=True)



