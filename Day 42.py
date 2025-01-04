#Day 42 - Class methods


#Create a class for a bank account with methods for deposit and withdrawal.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        """Initialize the bank account with an account holder's name and a starting balance."""
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account."""
        if amount > self.balance:
            print(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance


# Example usage:
account = BankAccount("John Doe", 1000)  # Create an account with a starting balance of 1000
account.deposit(500)                     # Deposit 500
account.withdraw(200)                    # Withdraw 200
print(f"Final balance: {account.get_balance()}")  # Check balance
