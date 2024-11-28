#Day 5 - Conditional Statements

#Note : Run these codes one by one 

#1. Write a program that reads an integer as user 
# input and prints whether the number is Odd or 
# Even to the console

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


#2. Write a program that takes three numbers as 
# input and prints the largest among them.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")


#3. Write a program that checks if a given input 
# year is a leap year or not

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#4. Write a program that reads the percentage and 
# then prints their corresponding letter grade 
# (A, B, C, D, or F)

percentage = float(input("Enter the percentage: "))

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The letter grade is {grade}")