#Day 3 - Input and Output

#program to read user input and print it to the console

#name = input("Enter your name: ")
#print("Your name:", name)

#modified program for different data type 
#for string data type
name = input("Enter your name: ")
print("Your name:", name)

# for an integer data type
age = int(input("Enter your age: "))
print("Your age:", age)

# for a float data type 
height = float(input("Enter your height in meters: "))
print("Your height:", height)

# for a boolean data type 
likes_python = input("Do you like Python? (yes/no): ").strip().lower() == "yes"
print("Likes Python:", likes_python)


