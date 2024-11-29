#Day 6 - Calculate the area of a circle.

#Q. Write a program that takes radius of the 
# circle and outputs the area of the circle to 
# 2 decimal digits

import math

radius = float(input("Enter the radius of the circle:"))

pi  = 3.14159

area = pi * radius ** 2

print(f"The area of the circle is: {area}")

