#Day 70: Numerical computing

#Use NumPy for numerical computing.

import numpy as np

# Creating Arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
randoms = np.random.rand(3, 2)

# Array Operations
a, b = np.array([10, 20, 30]), np.array([1, 2, 3])
add, subtract, multiply, divide = a + b, a - b, a * b, a / b

# Math Functions
angles = np.array([0, np.pi/2, np.pi])
sin_values, cos_values = np.sin(angles), np.cos(angles)
exp_values, log_values = np.exp([1, 2, 3]), np.log([1, np.e, np.e**2])

# Aggregations
data = np.array([5, 10, 15, 20, 25])
total, mean, median, std_dev = np.sum(data), np.mean(data), np.median(data), np.std(data)

# Reshaping and Slicing
arr = np.arange(12).reshape(3, 4)
slice1, slice2 = arr[2, :], arr[:, 1]

# Linear Algebra
A, B = np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])
dot_product, transpose, inverse, determinant = np.dot(A, B), A.T, np.linalg.inv(A), np.linalg.det(A)

# Practice Task
rand_matrix = np.random.randint(1, 100, (4, 4))
row_sum, col_sum = np.sum(rand_matrix, axis=1), np.sum(rand_matrix, axis=0)
normalized = (rand_matrix - np.mean(rand_matrix)) / np.std(rand_matrix)

print("Matrix:\n", rand_matrix)
print("Row Sum:", row_sum, "\nColumn Sum:", col_sum)
print("Normalized Matrix:\n", normalized)
