class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied. Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"


acc = BankAccount("Zhansiya", 100)

print(acc)  

acc.deposit(50)     # Баланс 150
acc.deposit(200)    # Баланс 350

acc.withdraw(100)   # Баланс 250
acc.withdraw(500)   # ❌ болмайды
acc.withdraw(-20)   # ❌ болмайды

print(acc)  
