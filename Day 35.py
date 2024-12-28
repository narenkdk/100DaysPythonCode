def calculate_average(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip()]
        
        if not numbers:
            print("No numbers found in the file.")
            return None
        
        average = sum(numbers) / len(numbers)
        return average

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("The file contains non-numeric data.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify your file path
file_path = 'numbers.txt'  # Replace with your actual file path
average = calculate_average(file_path)

if average is not None:
    print(f"The average of numbers in the file is: {average}")
