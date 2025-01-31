#Day 69: Statistical analysis


#Perform statistical analysis on a dataset.

import pandas as pd
import numpy as np
import scipy.stats as stats

# Load dataset (replace with your dataset)
df = pd.read_csv("your_dataset.csv")

# Basic descriptive statistics
print("Summary Statistics:")
print(df.describe())

# Checking for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Correlation matrix
print("\nCorrelation Matrix:")
print(df.corr())

# Hypothesis testing (Example: t-test between two groups)
group1 = df[df['Category'] == 'A']['Value']
group2 = df[df['Category'] == 'B']['Value']

t_stat, p_value = stats.ttest_ind(group1, group2, nan_policy='omit')
print(f"\nT-Test: t-statistic = {t_stat}, p-value = {p_value}")



# Normality test (Shapiro-Wilk)
stat, p = stats.shapiro(df['Value'].dropna())
print(f"\nShapiro-Wilk Test: Statistic={stat}, p-value={p}")

# ANOVA test (if multiple groups exist)
anova_stat, anova_p = stats.f_oneway(
    df[df['Category'] == 'A']['Value'], 
    df[df['Category'] == 'B']['Value'], 
    df[df['Category'] == 'C']['Value']
)
print(f"\nANOVA Test: F-statistic = {anova_stat}, p-value = {anova_p}")

# Chi-Square test (for categorical data)
contingency_table = pd.crosstab(df['Category'], df['Outcome'])
chi2_stat, chi2_p, _, _ = stats.chi2_contingency(contingency_table)
print(f"\nChi-Square Test: Chi2-statistic = {chi2_stat}, p-value = {chi2_p}")
