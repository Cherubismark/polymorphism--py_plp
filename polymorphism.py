class Animal:
    def move(self):
        print("Animals can move ")

class Dog(Animal):
    def move(self):
        print("Dog is running")

class Bird(Animal):
    def move(self):
        print("Bird is flying ")

class Vehicle:
    def move(self):
        print("Vehicles can move ")

class Car(Vehicle):
    def move(self):
        print("Car is driving ")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ")

# Polymorphism in action
things = [Dog(), Bird(), Car(), Plane()]

for thing in things:
    thing.move()

