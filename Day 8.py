#Day 8 - Simple Calculator

#Q Create a simple calculator program that can add, 
# subtract, multiply, and divide two integers


def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    

    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if choice == '1':
            print(f"The result of {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"The result of {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"The result of {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result of {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input! Please select a valid operation.")
        
        
calculator()
