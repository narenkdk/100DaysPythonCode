#Day 37 - Handle Exceptions II

#Handle exceptions for file not found.

try:
    # Attempt to open a file
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError as e:
    # Handle the file not found exception
    print(f"Error: {e}")
    print("The file you are trying to open does not exist. Please check the file path and try again.")
