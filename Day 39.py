#Day 39 - Class Object


#Create a class for a simple car with methods like start and stop.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False

    def start(self):
        if self.is_running:
            print(f"The {self.make} {self.model} is already running.")
        else:
            self.is_running = True
            print(f"The {self.make} {self.model} has started.")

    def stop(self):
        if not self.is_running:
            print(f"The {self.make} {self.model} is already stopped.")
        else:
            self.is_running = False
            print(f"The {self.make} {self.model} has stopped.")



# Example usage:
my_car = Car("Toyota", "Corolla")
my_car.start()
my_car.stop()
my_car.stop()
