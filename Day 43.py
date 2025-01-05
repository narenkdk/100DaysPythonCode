#Day 43 - Encapsulation


#Implement encapsulation in a class.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance  # Private attribute

    # Getter method for account_holder
    def get_account_holder(self):
        return self.__account_holder

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount!")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount!")

# Creating an instance of the class
account = BankAccount("Alice", 5000)

# Accessing private data using public methods
print("Account Holder:", account.get_account_holder())
print("Balance:", account.get_balance())

# Using methods to modify data
account.deposit(1500)
account.withdraw(3000)

# Attempt to directly access private attributes (This will raise an AttributeError)
# print(account.__balance)  # Uncommenting this line will cause an error

# Instead, use getter and setter methods
account.set_balance(8000)
print("Updated Balance:", account.get_balance())
