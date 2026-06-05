from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class SportsCar(Car):
    def __start_engine(self):
        print("Engine Started")

    def drive(self):
        self.__start_engine()
        print("Car is Moving")


car = SportsCar()
car.drive()