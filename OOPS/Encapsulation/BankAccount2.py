class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if(amount>0):
            self.__balance+=amount
        else:
            print("amount should be positive")
    def withdraw(self,amount):
        if(amount<self.__balance):
            self.__balance-=amount
        else:
            print("insufficient balance")

user=BankAccount(5000)
user.deposit(2000)
user.withdraw(100)
print(user.get_balance())