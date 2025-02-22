#Day 89: Generate fractals


#Write a program to generate fractals.

#Mandelbrot Set (Using Matplotlib)

import numpy as np
import matplotlib.pyplot as plt

# Function to check if a point belongs to the Mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iter

# Generate Mandelbrot fractal
def generate_mandelbrot(width, height, max_iter):
    xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    fractal = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            fractal[i, j] = mandelbrot(c, max_iter)

    return fractal

# Plot the Mandelbrot set
width, height, max_iter = 1000, 1000, 100
fractal = generate_mandelbrot(width, height, max_iter)

plt.figure(figsize=(10, 10))
plt.imshow(fractal, cmap="inferno", extent=(-2, 1, -1.5, 1.5))
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()


