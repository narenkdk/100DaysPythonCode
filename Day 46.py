#Day 46 - Class decorators


#Use class decorators in Python.

#define a class decorator 

def class_decorator(cls):
    #modify the class in some way 
    cls.decorated = True #add a new attribute
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"Creating an instance of {cls.__name__}")
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init #replace the original initializer
    return cls


#apply the class decorator 
@class_decorator 
class MyClass:
    def __init__(self, name):
        self.name = name


#test the decorated class 
obj = MyClass("Test")
print(obj.name)
print(obj.decorated)
