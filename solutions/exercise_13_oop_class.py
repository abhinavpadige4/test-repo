\"\"\"
Exercise 13: Object-Oriented Programming - Simple Class
Topic: OOP
Difficulty: Medium

Problem Statement:
Create a class `BankAccount` that has attributes for account number, account holder name, and balance.
Include methods to deposit, withdraw, and display the balance. Ensure that the balance cannot go negative.

Solution:
\"\"\"
class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Balance for {self.account_holder} (Account #{self.account_number}): ${self.balance}")

def main():
    # Example usage
    account = BankAccount("123456", "John Doe", 1000)
    account.display_balance()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)  # Should fail
    account.display_balance()

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Initial balance
    acc = BankAccount("111", "Alice", 500)
    assert acc.balance == 500, "Test 1 failed: Initial balance"
    print("Test Case 1 Passed: Initial balance")
    
    # Test Case 2: Deposit
    acc.deposit(200)
    assert acc.balance == 700, "Test 2 failed: Deposit"
    print("Test Case 2 Passed: Deposit")
    
    # Test Case 3: Withdrawal
    acc.withdraw(300)
    assert acc.balance == 400, "Test 3 failed: Withdrawal"
    print("Test Case 3 Passed: Withdrawal")
    
    # Test Case 4: Withdrawal exceeding balance
    # We capture print output? For simplicity, we just check balance doesn't change
    initial = acc.balance
    acc.withdraw(5000)  # Should not change balance
    assert acc.balance == initial, "Test 4 failed: Overdraw should not change balance"
    print("Test Case 4 Passed: Overdraw protection")
    
    # Test Case 5: Negative deposit
    acc.deposit(-50)  # Should not change balance
    assert acc.balance == initial, "Test 5 failed: Negative deposit should not change balance"
    print("Test Case 5 Passed: Negative deposit protection")
    
    print("\\nAll tests passed!")