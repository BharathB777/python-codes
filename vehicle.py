class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


class Truck(Vehicle):
    pass


car = Car("Toyota", 180)
bike = Bike("Yamaha", 120)
truck = Truck("Volvo", 100)

print(car.brand, car.speed)
print(bike.brand, bike.speed)
print(truck.brand, truck.speed)