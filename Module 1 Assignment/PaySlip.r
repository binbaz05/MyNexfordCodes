set.seed(123)

# Create a list of 400 employees dynamically

employees <- list()

for (e in 1:400) {
  employee <- list(
    emp_id = e,
    emp_name = paste("Emp_", e, sep = ""),
    emp_salary = sample(3000:90000, 1), # Random salary between 3000 and 90000
    emp_gender = sample(c("Male", "Female"), 1) # Randomly assign gender
  )
  employees[[e]] <- employee
}

# Function to generate payment slips and determine employee employement Levels

generate_payslip <- function(employee) {
  tryCatch({
    id <- employee$emp_id
    name <- employee$emp_name
    gender <- employee$emp_gender
    salary <- employee$emp_salary

    employee_level <- "None"

    # Condition to assign employee level based on salary and gender
    if (salary > 7500 && salary < 30000 && gender == "Female") {
      employee_level <- "A5-F"
    }

    if (salary > 10000 && salary < 20000) {
      employee_level <- "A1"
    }

    # Print payment slip for the employee
    print(paste("Payment Slip for employee", id))
    print(paste("Name:", name))
    print(paste("Gender:", gender))
    print(paste("Salary:", salary))
    print(paste("Employee Level:", employee_level))
    print("------------------------------")

  }, error = function(e) {
    # Exception to handle potential errors
    print(paste("Error generating pay slip for employeeID:", employee$emp_id))
    print("Error details:", e$message)
  })
}

for (employee in employees) {
  generate_payslip(employee)
}