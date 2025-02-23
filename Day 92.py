#Day 92: Design patterns


#Study and implement design patterns in Python.

#Here are two examples of design patterns in Python:

#1. Singleton Patternclass Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Testing
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True


#2. Factory Pattern
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        return None

# Testing
animal = AnimalFactory.get_animal("dog")
print(animal.speak())  # Woof!
