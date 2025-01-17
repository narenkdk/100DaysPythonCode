#Day 55 - Iterable class.


#Implement a custom iterable class.

class CustomRange:
    def __init__(self, start, end):
        """Initialize the range with start and end values."""
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next value in the range or raise StopIteration."""
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# Using the CustomRange class
custom_range = CustomRange(1, 5)

for number in custom_range:
    print(number)

# Output:
# 1
# 2
# 3
# 4
