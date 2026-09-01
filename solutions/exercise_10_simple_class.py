\"\"\"
Exercise 10: Simple Class (OOP)
Topic: Object-Oriented Programming
Difficulty: Medium

Problem Statement:
Create a class called `BankAccount` that simulates a simple bank account.
The class should have:
- Attributes: account_number, account_holder_name, balance
- Methods: 
    * __init__: to initialize the account with account number, holder name, and initial balance (default 0)
    * deposit(amount): to add money to the account
    * withdraw(amount): to withdraw money from the account (if sufficient balance)
    * get_balance(): to return the current balance
    * display(): to print the account details

The program should:
- Ask the user to enter account details (account number, holder name, initial balance)
- Create a BankAccount object
- Allow the user to perform transactions (deposit, withdraw, check balance) until they choose to exit

Example:
Enter account number: 12345
Enter account holder name: John Doe
Enter initial balance: 1000

Options:
1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit

Choose an option: 1
Enter amount to deposit: 500
Deposit successful.

Choose an option: 2
Enter amount to withdraw: 200
Withdrawal successful.

Choose an option: 3
Current balance: 1300
\"\"\"

class BankAccount:
    \"\"\"A simple bank account class.\"\"\"
    
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    
    def deposit(self, amount):
        \"\"\"Deposit money into the account.\"\"\"
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount):
        \"\"\"Withdraw money from the account if sufficient balance.\"\"\"
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        \"\"\"Return the current balance.\"\"\"
        return self.balance
    
    def display(self):
        \"\"\"Display the account details.\"\"\"
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Balance: ${self.balance:.2f}")

def main():
    print("Welcome to the Bank Account System")
    try:
        acc_num = input("Enter account number: ")
        acc_name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Error: Initial balance must be a number.")
        return
    
    account = BankAccount(acc_num, acc_name, initial_balance)
    
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Display Account Details")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                if account.deposit(amount):
                    print("Deposit successful.")
                else:
                    print("Error: Deposit amount must be positive.")
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Error: Insufficient balance or invalid amount.")
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '3':
            print(f"Current balance: ${account.get_balance():.2f}")
        elif choice == '4':
            account.display()
        elif choice == '5':
            print("Thank you for using the Bank Account System. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    # Test BankAccount class
    acc = BankAccount("123", "Test User", 100)
    assert acc.get_balance() == 100
    assert acc.deposit(50) == True
    assert acc.get_balance() == 150
    assert acc.withdraw(30) == True
    assert acc.get_balance() == 120
    assert acc.withdraw(200) == False  # Insufficient funds
    assert acc.get_balance() == 120
    assert acc.deposit(-10) == False  # Negative deposit
    assert acc.get_balance() == 120
    
    print("All unit tests passed.")
    
    # Uncomment below to run interactively
    # main()