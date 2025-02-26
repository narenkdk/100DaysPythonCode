#Day 95: Metaclasses

#Explore advanced topics like metaclasses.

#A demonestration of metaclasses in Python

# Defining a custom metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with Meta")
        dct["created_by"] = "MetaClass"
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        print(f"Creating an instance of {cls.__name__}")
        return super().__call__(*args, **kwargs)

# Creating a class using the custom metaclass
class MyClass(metaclass=Meta):
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value: {self.value}, Created by: {self.created_by}")

# Instantiating the class
obj = MyClass(42)
obj.show()

