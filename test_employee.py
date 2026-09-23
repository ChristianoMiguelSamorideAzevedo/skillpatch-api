from services.employee_service import (
    create_employee,
    get_all_employees
)

create_employee(
    "Miguel Samori",
    "miguel@email.com",
    "Academy Analyst"
)

employees = get_all_employees()

print(employees)
