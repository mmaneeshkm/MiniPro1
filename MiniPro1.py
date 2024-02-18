class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Account Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New Balance: ${self.balance}")

def login():
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    # Check if the account exists
    if account_number in accounts and accounts[account_number].pin == pin:
        return accounts[account_number]
    else:
        print("Invalid account number or PIN. Please try again.")
        return login()

def main():
    print("Welcome to the Banking System")

    while True:
        print("\nOptions:")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account = login()

            if account:
                while True:
                    print("\nOptions:")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")

                    option = input("Enter your option: ")

                    if option == '1':
                        account.check_balance()
                    elif option == '2':
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                    elif option == '3':
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                    elif option == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option. Try again.")

        elif choice == '2':
            print("Thank you. Visit Again.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    accounts = {
        '123456789': BankAccount('123456789', '1234', 1000),
        '987654321': BankAccount('987654321', '4321', 500)
    }
    main()
