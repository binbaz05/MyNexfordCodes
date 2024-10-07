import random

# This section create a list of 400 employees

employees = []
for e in range(1, 401):
    employee = {
        "emp_id": e,
        "emp_name": f"Emp_{e}",
        "emp_salary": random.randint(3000,90000),
        "emp_gender": random.choice(["Male","Female"])
    }
    employees.append(employee)

#  Implement condition for Employement Level based on salary

for employee in employees:
    try:
        employee_level = "None"
        salary = employee['emp_salary']
        gender = employee['emp_gender']

        if (salary < 10000) and (salary < 20000):
            employee_level = "A1"

        if (salary < 7500) and (salary < 30000) and gender == "Female":
            employee_level = "A5-F"
        
        # Generate employees payment slip

        print(f"Payment Slip for {employee['emp_name']} (ID: {employee['emp_id']})")
        print(f"Salary: ${salary}")
        print(f"Gender: {gender}")
        print(f"Employee Level: {employee_level}")
        print("-" * 40)
    except Exception as e:
        # Exception handling for potential errors

        print(f"Error generating slip for {employee['emp_name']} (ID: {employee['emp_id']}): {str(e)}")
