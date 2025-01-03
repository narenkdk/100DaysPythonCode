# Day 41 - Inheritance


#Implement inheritance between classes.

# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def get_info(self):
        return f"{self.name} is a {self.species}."

# Subclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call the parent class's __init__
        self.breed = breed
    
    # Overriding the parent method
    def make_sound(self):
        return "Woof!"
    
    # Adding a new method specific to the subclass
    def fetch(self):
        return f"{self.name} is fetching the ball!"

# Another subclass
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed
    
    # Overriding the parent method
    def make_sound(self):
        return "Meow!"
    
    # Adding a new method
    def climb(self):
        return f"{self.name} is climbing a tree!"

# Using the classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")

print(dog.get_info())  # Buddy is a Dog.
print(dog.make_sound())  # Woof!
print(dog.fetch())  # Buddy is fetching the ball!

print(cat.get_info())  # Whiskers is a Cat.
print(cat.make_sound())  # Meow!
print(cat.climb())  # Whiskers is climbing a tree!
