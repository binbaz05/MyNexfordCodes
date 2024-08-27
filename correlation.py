import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the data
data = pd.read_csv('/Users/binbaz/Downloads/Employee_data.csv')

# Clean the data: Remove dollar signs and commas, convert to numeric
data['salary'] = data['salary'].replace('[\$,]', '', regex=True).astype(float)
data['salbegin'] = data['salbegin'].replace('[\$,]', '', regex=True).astype(float)

# Filter data for male employees
male_data = data[data['gender'] == 'm']

# Plot the data and fit a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='salbegin', y='salary', data=male_data)
plt.xlabel('Beginning Salary ($)')
plt.ylabel('Current Salary ($)')
plt.title('Beginning Salary vs. Current Salary for Male Employees')
plt.grid(True)
plt.show()
# final path of the code.
# This another change.
# This is third change.
# this is fourth change.