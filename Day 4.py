#Day 4 - Arithmetic Operations 

#Q. 1. Write a program that declares two integer 
# variables and perform basic arithmetic operations 
# (addition, subtraction, multiplication, division) 
# on them. Print the results to the console.

#declaring two integer variables 
a = 10 
b = 5

#performing arithmetic operations 
add = a + b
sub = a - b
mul = a * b
div = a / b

print ("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)


#Q. 2. Write a program that calculates the area of 
# #a rectangle. Prompt the user to input the 
# length(integer) and width(integer) of the 
# rectangle, calculate the area (length * width), 
# and print the result.

length = int(input("Enter the length of the rectangle (integer): "))
width = int(input("Enter the width of the rectangle (integer): "))


area = length * width


print(f"The area of the rectangle is: {area}")

#Q. 3. Modify the above program to read decimal 
# numbers as the length and width, and output the 
# area to two decimal points. 

length = float(input("Enter the length of the rectangle (decimal): "))
width = float(input("Enter the width of the rectangle (decimal): "))

area = length * width

print(f"The area of the rectangle is: {area:.2f}")
