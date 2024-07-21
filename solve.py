# part 1
import pandas as pd
import numpy as np

# Generate random data
np.random.seed(0)
data = np.random.randint(10, 100, size=(4, 6))

# Create DataFrame
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F'], index=['Jane', 'Mary', 'Bob', 'Mark'])

# Display the DataFrame
print("Data frame of random numbers")
print(df)


# part 2
# Calculate row totals
row_totals = df.sum(axis=1)

# Calculate column totals
column_totals = df.sum(axis=0)

# Display row totals
print("\nData frame row totals")
print(row_totals)

# Display column totals
print("\nData frame column totals")
print(column_totals)

# part 3
# Calculate mean of row totals
mean_row_totals = row_totals.mean()

# Calculate mean of column totals
mean_column_totals = column_totals.mean()

# Display means
print("\nMean of data frame row totals:", mean_row_totals)
print("Mean of data frame column totals:", mean_column_totals)


#part 4
# Load the salary data
salary_data = pd.read_csv('C:/Users/braisonW/Desktop/G/salary/salary.csv')

# Calculate average salary by year
average_salary_by_year = salary_data.groupby('year')['salary'].mean()

# Display the result
print("\nAverage salary by year")
print(average_salary_by_year)


#part 5
# Calculate average salary by organization within year
average_salary_by_org_within_year = salary_data.groupby(['year', 'organization'])['salary'].mean()

# Display the result
print("\nAverage salary by organization within year")
print(average_salary_by_org_within_year)

# part 6
# Filter data for fire fighters
fire_fighters_data = salary_data[salary_data['job'].str.contains('Firefighter')]

# Calculate average salary and count by year
average_salary_and_count_firefighters = fire_fighters_data.groupby('year').agg({'salary': 'mean', 'job': 'count'}).rename(columns={'job': 'count'})

# Display the result
print("\nAverage salary and total number of firefighters by year")
print(average_salary_and_count_firefighters)

# part 7
# Create a pivot table
pivot_table = salary_data.pivot_table(values='salary', index='jobCategory', columns='year', aggfunc='mean')

# Display the pivot table
print("\nPivot table of mean salary by job category and year")
print(pivot_table)
