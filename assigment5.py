import sys

bank_balance = 10000
accounts = []
transactions = []


def create_account(name, initial_balance=0, account_type="Savings"):
    account = {
        "name": name,
        "balance": initial_balance,
        "account_type": account_type
    }
    accounts.append(account)
    return account

def deposit(balance, amount):
    if amount <= 0:
        return balance, "Invalid deposit amount"
    balance += amount
    return balance, "Amount Deposited Successfully"

def withdraw(balance, amount):
    if amount <= 0:
        return balance, "Invalid withdrawal amount"
    if amount > balance:
        return balance, "Insufficient Balance"
    balance -= amount
    return balance, "Amount Withdrawn Successfully"

def check_balance(balance):
    return balance


def transaction_history(*transactions):
    print("\n----- TRANSACTION HISTORY -----")
    if len(transactions) == 0:
        print("No transactions available")
        return
    for transaction in transactions:
        print(transaction)

def customer_details(**data):
    print("\n----- CUSTOMER DETAILS -----")

    for key, value in data.items():
        print(f"{key}: {value}")

def loan_eligibility(balance, salary):
    if balance >= 10000 and salary >= 25000:
        return "Eligible for Loan"
    else:
        return "Not Eligible for Loan"

def display_message():
    print("Welcome to Online Banking System")

def update_global_balance(amount):
    global bank_balance
    bank_balance += amount
    return bank_balance

def enclosing_scope_demo():
    balance = 1000
    def modify_balance():
        nonlocal balance
        balance += 500
    modify_balance()
    return balance

name = "Global Name"

def legb_demo():
    name = "Enclosing Name"
    def inner():
        name = "Local Name"
        print("\n----- LEGB DEMONSTRATION -----")
        print("Local:", name)
        print("Built-in len():", len("BANK"))
    inner()
    print("Enclosing:", name)

gst = lambda amount: amount * 0.18
interest = lambda amount: amount * 0.05
sort_balance = lambda account: account["balance"]

def verify_pin(correct_pin, attempts=1):
    print(f"PIN Verification Attempt: {attempts}")
    if entered_pin == correct_pin:
        print("PIN Verified Successfully")
        return True
    if attempts >= 3:
        print("Maximum Attempts Reached")
        return False
    return verify_pin(correct_pin, attempts + 1)

def compound_interest(principal, rate, years):
    if years == 0:
        return principal
    return compound_interest(
        principal * (1 + rate),
        rate,
        years - 1
    )

def countdown(n):
    if n == 0:
        print("Transaction Started")
        return
    print(n)
    countdown(n - 1)

def functional_programming_demo():
    balances = [5000, 15000, 20000, 8000, 25000]
    print("\n----- FUNCTIONAL PROGRAMMING -----")
    interest_values = list(map(interest, balances))
    print("Balances:")
    print(balances)
    print("Interest using map() and lambda:")
    print(interest_values)
    high_balance = list(
        filter(lambda balance: balance > 10000, balances)
    )
    print("\nAccounts with Balance > 10000:")
    print(high_balance)
    sorted_balances = sorted(balances)
    print("\nSorted Balances:")
    print(sorted_balances)

def builtin_functions_demo():
    balances = [5000, 15000, 20000, 8000, 25000]
    print("\n----- BUILT-IN FUNCTIONS -----")
    print("Number of accounts:", len(balances))
    print("Total Balance:", sum(balances))
    print("Maximum Balance:", max(balances))
    print("Minimum Balance:", min(balances))
    print("Average Balance:", round(sum(balances) / len(balances), 2))

def argument_demo():
    print("\n----- ARGUMENT TYPES -----")
    balance1, status1 = deposit(5000, 1000)
    print("Positional Arguments:")
    print("Updated Balance:", balance1)
    print("Status:", status1)
    balance2, status2 = deposit(
        amount=2000,
        balance=5000
    )
    print("\nKeyword Arguments:")
    print("Updated Balance:", balance2)
    print("Status:", status2)
    account = create_account(
        "Default Customer"
    )
    print("\nDefault Argument:")
    print(account)

def print_vs_return_demo():
    print("\n----- PRINT VS RETURN -----")
    display_message()
    balance = check_balance(15000)
    print("Returned Balance:", balance)
    result = display_message()
    print("Return value of display_message():", result)

def banking_system():
    global bank_balance
    current_balance = bank_balance
    current_transactions = []
    while True:
        print("\n")
        print("=" * 45)
        print("        ONLINE BANKING MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Loan Eligibility Check")
        print("7. Functional Programming Demo")
        print("8. Recursion Demo")
        print("9. Account Details")
        print("10. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            name = input("Enter Customer Name: ")
            account_type = input(
                "Enter Account Type (Savings/Current): "
            )
            initial_balance = float(
                input("Enter Initial Balance: ")
            )
            account = create_account(
                name,
                initial_balance,
                account_type
            )
            current_balance = initial_balance
            print("\nAccount Created Successfully")
            print("Account Details:")
            print("Name:", account["name"])
            print("Account Type:", account["account_type"])
            print("Balance:", account["balance"])

        elif choice == "2":
            amount = float(
                input("Enter Deposit Amount: ")
            )
            current_balance, status = deposit(
                current_balance,
                amount
            )
            print("\n", status)
            print("Updated Balance:", current_balance)
            if status == "Amount Deposited Successfully":
                current_transactions.append(
                    f"Deposited: ₹{amount}"
                )
                bank_balance = update_global_balance(amount)
                interest_amount = interest(amount)
                print(
                    "Interest Calculation using Lambda:",
                    interest_amount
                )
                print(
                    "GST using Lambda:",
                    gst(amount)
                )
        elif choice == "3":
            amount = float(
                input("Enter Withdrawal Amount: ")
            )
            current_balance, status = withdraw(
                current_balance,
                amount
            )
            print("\n", status)
            print("Updated Balance:", current_balance)
            if status == "Amount Withdrawn Successfully":
                current_transactions.append(
                    f"Withdrawn: ₹{amount}"
                )
        elif choice == "4":
            balance = check_balance(
                current_balance
            )
            print("\nCurrent Balance:", balance)
        elif choice == "5":
            transaction_history(
                *current_transactions
            )
        elif choice == "6":
            salary = float(
                input("Enter Monthly Salary: ")
            )
            result = loan_eligibility(
                current_balance,
                salary
            )
            print("\nLoan Eligibility:", result)
        elif choice == "7":
            functional_programming_demo()
            if accounts:
                sorted_accounts = sorted(
                    accounts,
                    key=sort_balance
                )
                print("\n----- SORTED ACCOUNT LIST -----")
                for account in sorted_accounts:
                    print(
                        account["name"],
                        "-> ₹",
                        account["balance"]
                    )
        elif choice == "8":
            print("\n----- RECURSION DEMONSTRATION -----")
            print("\nTransaction Countdown:")
            countdown(3)
            print("\nCompound Interest:")
            principal = float(
                input("Enter Principal Amount: ")
            )
            rate = float(
                input("Enter Interest Rate (%): ")
            ) / 100
            years = int(
                input("Enter Number of Years: ")
            )
            final_amount = compound_interest(
                principal,
                rate,
                years
            )
            print(
                "Final Amount:",
                round(final_amount, 2)
            )
            print("\nPIN Verification:")
            verify_pin("1234")
            print(
                "\nPython Recursion Limit:",
                sys.getrecursionlimit()
            )
        elif choice == "9":
            name = input("Enter Customer Name: ")
            customer_details(
                name=name,
                account_type="Savings",
                balance=current_balance
            )
            print(
                "\nEnclosing Scope Balance:",
                enclosing_scope_demo()
            )
            legb_demo()
            argument_demo()
            print_vs_return_demo()
            builtin_functions_demo()
        elif choice == "10":
            print("\nThank you for using Online Banking System.")
            break
        else:
            print("\nInvalid Choice. Please try again.")


banking_system()