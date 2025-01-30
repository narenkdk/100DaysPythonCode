#Day 68: Matplotlib

#Create data visualizations using Matplotlib.




import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)

# 1. Line Plot
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st plot
plt.plot(x, y, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# 2. Scatter Plot
plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd plot
plt.scatter(x, y, color='blue', label='sin(x)', alpha=0.7)
plt.scatter(x, y2, color='red', label='cos(x)', alpha=0.7)
plt.title('Scatter Plot of Sine and Cosine')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# 3. Histogram
plt.subplot(2, 2, 3)  # 2 rows, 2 columns, 3rd plot
data = np.random.randn(1000)
plt.hist(data, bins=30, color='green', edgecolor='black')
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 4. Bar Plot
plt.subplot(2, 2, 4)  # 2 rows, 2 columns, 4th plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 4, 6]
plt.bar(categories, values, color='orange')
plt.title('Bar Plot of Categories')
plt.xlabel('Category')
plt.ylabel('Value')

# Show the plots
plt.tight_layout()  # Adjust the layout
plt.show()
