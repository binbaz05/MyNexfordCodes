Employee Salary Function

Overview

This Python script is designed to manage and retrieve employee salary data from a CSV file. It allows users to:

    Load employee salary records from a CSV file.
    Search for an employee by name and display their details.
    Export employee details to a CSV file.
    Archive the exported employee details in a zip file.

The script also includes error handling for common issues such as missing files or non-existent employee records.

Prerequisites

Ensure you have the following installed before running the script:

    Jupyter notebook server
    Pandas library
    OS module (comes pre-installed with Python)
    CSV module (comes pre-installed with Python)
    zipfile module (comes pre-installed with Python)

|-- salaryfunction.ipynb  # The main Python script
|-- Total.csv   # CSV file containing employee data
|-- README.md    # Instructions on how to use the script
|-- <ZIP_ARCHIVE_FILES> # Generated zip files with employee details

How to Use

1. Ensure that the 'Total.csv' file is in the same directory as the jupyter notebook file, and update the path in the csv_file_path variable.
	
2. Run the salaryfunction.ipynb

3. The script will prompt for the employee Name and display the employee’s details, generate a CSV file and archive file using zip.







