from abc import abstractmethod,ABC

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPIPayment(PaymentMethod):
    def pay(self,amount):
        print(f"paid through upi {amount}")

class CashPayment(PaymentMethod):
    def pay(self,amount):
        print(f"paid through cash {amount}")

class WhatsappPayment(PaymentMethod):
    def pay(self,amount):
        print(f"paid through WAPay {amount}")

class RideBooking:
    def __init__(self,pay_method:PaymentMethod):
        self.pay_method=pay_method
    def pay_money(self,amount):
        self.pay_method.pay(amount)
        

upi=UPIPayment()
cash=CashPayment()
wa=WhatsappPayment()

user1=RideBooking(upi)
user2=RideBooking(cash)

user1.pay_money(100)
user2.pay_money(2000)