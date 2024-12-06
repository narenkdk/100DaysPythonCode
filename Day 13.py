#Day 13 - Largest of three numbers.

#Write a program to find the largest of three 
# numbers.

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    return largest

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find and display the largest number
largest_number = find_largest(num1, num2, num3)
print(f"The largest number is: {largest_number}")
