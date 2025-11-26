from ex import get_employee_detail

def test_get_employee_detail():
    output = get_employee_detail("Alice Smith", "E202", "HR", 60000)

    expected = (
        "Employee Name: Alice Smith, "
        "Employee ID: E202, "
        "Department: HR, "
        "Salary: 60000.00"
    )

    assert output == expected
