# employee Payment Slip Generator

This Python program dynamically generates a list of 400 employees and creates payment slips for each employee. The program uses conditional logic to assign an appropriate employee level based on the employee's salary and gender. Additionally, exception handling is implemented to catch any potential errors during the process.

## Features

- **Dynamic employee Creation**: Generates a list of 400 employees, each with a randomly assigned salary and gender.
- **Conditional Employee Level Assignment**:
  - If a employee's salary is between $10,000 and $20,000, their employee level is set to `"A1"`.
  - If a employee's salary is between $7,500 and $30,000 **and** they are female, their employee level is set to `"A5-F"`.
- **Exception Handling**: The program includes error handling to manage potential issues, such as incorrect data types or missing fields, preventing the program from crashing.

## Code Structure

### 1. employee List Generation

The program dynamically generates a list of 400 employees. Each employee is assigned:
- A unique `id` (1 to 400).
- A random salary between $3,000 and $90,000.
- A randomly assigned gender (`male` or `female`).

### 2. Payment Slip Generation

For each employee, the program:
- Prints a payment slip that includes the employee's ID, name, salary, gender, and employee level.
- Assigns employee levels based on the following conditions:
  - **Level A1**: Salary between $10,000 and $20,000.
  - **Level A5-F**: Salary between $7,500 and $30,000, and the employee is female.

### 3. Exception Handling

The program uses a `try-except` block to handle errors that may arise during the payment slip generation process. If an error occurs, an error message is printed, and the program moves on to the next employee.

## How to Run

1. Make sure you have Python installed (version 3.x).
2. Download or clone this repository.
3. Run the Python script `PaySlip.py` in your terminal or IDE.

```bash
python PaySlip.py
