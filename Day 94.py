#Day 94: Decorators and descriptors


#Experiment with decorators and descriptors.

# 1. Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()


#Decorator with Arguments

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()


#2. Descriptors

class Celsius:
    def __init__(self, value=0.0):
        self._temperature = value

    def __get__(self, instance, owner):
        print("Getting value...")
        return self._temperature

    def __set__(self, instance, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible!")
        self._temperature = value

class Temperature:
    celsius = Celsius()

temp = Temperature()
temp.celsius = 25  # Setting value...
print(temp.celsius)  # Getting value... 25

#Combining Decorators and Descriptors

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper

class Descriptor:
    def __init__(self, value=None):
        self.value = value

    @logger
    def __get__(self, instance, owner):
        return self.value

    @logger
    def __set__(self, instance, value):
        self.value = value

class Test:
    attribute = Descriptor()

t = Test()
t.attribute = 42  # Calling __set__ with (<__main__.Test object at ...>, 42)
print(t.attribute)  # Calling __get__ with (<__main__.Test object at ...>,) → 42

