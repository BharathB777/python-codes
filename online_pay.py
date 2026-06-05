from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


payment = UPI()
payment.pay(1000)