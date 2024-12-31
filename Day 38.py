#Day 38 - Custom Exceptions


#Create a custom exception class.

class CustomError(Exception):
    """Custom exception class for specific error handling."""
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

    def __str__(self):
        return f"Error Code {self.code}: {self.args[0]}"

# Example usage
def process_data(data):
    if not isinstance(data, list):
        raise CustomError("Data must be a list", 1001)
    if not data:
        raise CustomError("Data list is empty", 1002)
    print("Processing data:", data)

# Test the custom exception
try:
    process_data("not a list")
except CustomError as e:
    print(e)

try:
    process_data([])
except CustomError as e:
    print(e)
