# ATM System Using Functions

balance = float(input("Enter your account balance: ₹"))


def check_balance():
    print(f"\nCurrent Balance: ₹{balance:.2f}")


def deposit(amount):
    global balance
    balance += amount
    print(f"₹{amount:.2f} deposited successfully.")


def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
    else:
        print("Insufficient balance!")


def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))
        if amount > 0:
            deposit(amount)
        else:
            print("Please enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount > 0:
            withdraw(amount)
        else:
            print("Please enter a valid amount.")

    elif choice == "4":
        print("\nThank you for using the ATM. Have a nice day!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")