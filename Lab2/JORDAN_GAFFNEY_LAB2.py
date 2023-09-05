# TODO: Define BankAccount class
class BankAccount():      
# TODO: Define constructor with parameters to initialize instance attribute
    def __init__(self,name,checking,savings):
        self.checking_balance = savings
        self.savings_balance = checking
        self.name = name
# TODO: Define deposit_checking() method   
    def deposit_checking(self,amount):
        if amount < 0:
            print("Amount Must be positive")
            exit()
        else:
            self.checking_balance += amount
# TODO: Define deposit_savings() method   
    def deposit_savings(self,amount):
        if amount < 0:
            print("Amount Must be positive")
            exit()
        self.savings_balance += amount  
# TODO: Define withdraw_checking()  method
    def withdraw_checking(self,amount):
        if amount < 0:
            print("Amount Must be positive")
            exit()
        else:    
            self.checking_balance -= amount                    
# TODO: Define withdraw_savings()  method 
    def withdraw_savings(self,amount):
        if amount < 0:
            print("Amount Must be positive")
            exit()
        else:
            self.savings_balance -= amount  
# TODO: Define transfer_to_savings() method
    def transfer_to_savings(self,amount):
        if amount < 0:
            print("Amount Must be positive")
            exit()
        else:        
            self.checking_balance -= amount
            self.savings_balance += amount
#Demo code
account = BankAccount("Mickey", 500.00, 1000.00)    
account.checking_balance = 500    
account.savings_balance = 500    
account.withdraw_savings(100)    
account.withdraw_checking(100)    
account.transfer_to_savings(300)    
print(account.name)    
print(f'${account.checking_balance:.2f}')    
print(f'${account.savings_balance:.2f}')
