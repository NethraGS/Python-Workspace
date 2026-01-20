class BankAccount:
    def __init__(self,initial_balance,pin):
        self.__balance=initial_balance
        self.__pin=pin
        self._withdrawn_today=0
        self._dailylimit=30000
        self.__transactions=[]
    
    def __verify_pin(self,entered_pin):
        return self.__pin==entered_pin
    
    def __can_withdraw(self,amount):
        return (self._withdrawn_today+amount<=self._dailylimit)
         

    def __add_transactions(self,mess):
        self.__transactions.append(mess)
    
    def deposit(self,amount,pin):
        if not self.__verify_pin(pin):
            print("incorrect pin")
            return
        if(amount<0):
            print("not possible")
            return
        if(amount>0):
            self.__balance+=amount
            self.__add_transactions(f"deposited {amount}")
            print(f"deposited {amount}")
    
    def withdraw(self,amount,pin):
        if not self.__verify_pin(pin):
            print("incorrect pin")
            return
        if not self.__can_withdraw(amount):
            print("limit exceeded")
            return
        
        self.__balance-=amount
        self._withdrawn_today+=amount
        self.__add_transactions(f"withdrawn {amount}")
        print(f"withdrawn {amount}")
    def show_transactions(self,pin):
        if not self.__verify_pin(pin):
            print("incorrect pin")
            return
        for t in self.__transactions:
            print(t)


    

user1=BankAccount(20000,1234)
user1.deposit(100,1234)
user1.withdraw(100,1234)
user1.show_transactions(1234)


    

        

