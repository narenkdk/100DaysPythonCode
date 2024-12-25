#Day 32 - File operations: Read

#Read and display the contents of a text file.

# Specify the file path
file_path = 'example.txt'  # Replace with the path to your file

try:
    # Open the file in read mode and display its contents
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
