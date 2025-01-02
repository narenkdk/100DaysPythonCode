#Day 40 - Class hierarchy

#Create a class hierarchy for different shapes (circle, square, triangle).


from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Abstract base class for all shapes."""
    
    @abstractmethod
    def area(self):
        """Calculates and returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter of the shape."""
        pass

class Circle(Shape):
    """Represents a circle."""
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Square(Shape):
    """Represents a square."""
    
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    """Represents a triangle."""
    
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

# Example usage
shapes = [
    Circle(5),
    Square(4),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")
    print()
