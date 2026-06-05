from abc import ABC, abstractmethod

class Customer:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def get_name(self):
        return self.__name


class PremiumCustomer(Customer):
    def __init__(self, name, phone, membership):
        super().__init__(name, phone)
        self.membership = membership


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class Delivery:
    def calculate_charge(self):
        pass


class BikeDelivery(Delivery):
    def calculate_charge(self):
        return 40


class CarDelivery(Delivery):
    def calculate_charge(self):
        return 80


customer = PremiumCustomer("John", "9876543210", "Gold")
payment = UPI()
delivery = BikeDelivery()

payment.pay(500)
print("Delivery Charge:", delivery.calculate_charge())