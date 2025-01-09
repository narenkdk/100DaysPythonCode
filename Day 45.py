#Day 45 - Polymorphism


#Implement polymorphism with a shape area calculator.

from math import pi

# Base class
class Shape:
    def area(self):
        pass

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Function to calculate the area of any shape
def calculate_area(shape: Shape):
    print(f"The area of the shape is: {shape.area()}")

# Testing the polymorphism
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)

calculate_area(circle)       # Polymorphism in action
calculate_area(rectangle)
calculate_area(triangle)

