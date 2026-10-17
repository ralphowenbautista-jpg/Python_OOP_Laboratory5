
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed  # Encapsulation

    def start(self):  # Abstraction
        print("Vehicle is starting.")


class Car(Vehicle):  # Inheritance
    def start(self):  # Polymorphism
        print("Car engine is starting.")


# Create objects
vehicle = Vehicle("Toyota", 100)
car = Car("Honda", 120)

vehicle.start()
car.start()
