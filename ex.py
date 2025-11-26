# ex.py

def get_employee_detail(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}, "
        f"Employee ID: {emp_id}, "
        f"Department: {department}, "
        f"Salary: {salary:.2f}"
    )


if __name__ == "__main__":
    result = get_employee_detail("John Doe", 101, "HR", 50000)
    print(result)
