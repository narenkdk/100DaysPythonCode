#Day 83: Command-line tool


#Create a command-line tool with argparse.

import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    parser = argparse.ArgumentParser(description="A simple command-line calculator")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.num1, args.num2)
    elif args.operation == "subtract":
        result = subtract(args.num1, args.num2)
    elif args.operation == "multiply":
        result = multiply(args.num1, args.num2)
    elif args.operation == "divide":
        result = divide(args.num1, args.num2)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()



#How to use 
python calculator.py 10 5 add


#Output 
Result: 15.0
