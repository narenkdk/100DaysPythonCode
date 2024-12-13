#Day 20 - Fibonacci sequence

#Write a function to calculate the Fibonacci sequence up to a certain limit.

def fibonacci_sequence(limit):
    """
    Generate a Fibonacci sequence up to a given limit.

    Args:
        limit (int): The maximum value up to which the Fibonacci sequence is generated.

    Returns:
        list: A list containing the Fibonacci sequence up to the limit.
    """
    if limit < 0:
        raise ValueError("Limit must be a non-negative integer.")

    sequence = []
    a, b = 0, 1

    while a <= limit:
        sequence.append(a)
        a, b = b, a + b

    return sequence

# Example usage:
if __name__ == "__main__":
    limit = 100  # Adjust the limit as needed
    print(f"Fibonacci sequence up to {limit}: {fibonacci_sequence(limit)}")

