class BankAccount() :
    balance = 0.0
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0.0

    def deposit(self, amount) :
        self.balance += amount
        print("Balance Added Successfully.")
        print(f"Balance: {self.balance}")
    
    def withdraw(self, amount) :
        if amount > self.balance :
            print("Insufficient Funds")
        else :
            self.balance -= amount
            print("Balance Deduced.")
            print(f"Balance: {self.balance}")

owner_1 = BankAccount("Khan")
print(f"Owner name: {owner_1.owner_name}")
owner_1.deposit(10000)
owner_1.withdraw(5000)
owner_1.deposit(1000)


print(f"Remaining Balance: {owner_1.balance}")