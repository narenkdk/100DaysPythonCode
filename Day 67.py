#Day 67: Pandas


#Load and manipulate data using Pandas.

import pandas as pd

# Load data from a CSV file
df = pd.read_csv('data.csv')

# Show the original data
print("Original Data:")
print(df)

# Manipulate the data
# Add a new column
df['Country'] = ['USA', 'UK', 'Canada', 'Australia']

# Filter the data (e.g., only females)
females = df[df['Gender'] == 'Female']
print("\nFiltered Data (Females):")
print(females)

# Group the data by Gender and calculate the average age
avg_age_by_gender = df.groupby('Gender')['Age'].mean()
print("\nAverage Age by Gender:")
print(avg_age_by_gender)

# Sort the data by Age
sorted_by_age = df.sort_values(by='Age', ascending=True)
print("\nSorted by Age:")
print(sorted_by_age)

# Save the manipulated data to a new CSV file
df.to_csv('manipulated_data.csv', index=False)

print("\nManipulated data saved to 'manipulated_data.csv'")
