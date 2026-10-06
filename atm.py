def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Exit")


def withdraw(balance):
    try:
        amount = float(input("Enter withdrawal amount: ₹"))
    except ValueError:
        print("Please enter a valid number.")
        return balance

    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdrawal successful.")
        print(f"Remaining balance: ₹{balance:,.2f}")

    return balance


def main():
    balance = 10000.00

    print("Welcome to Python ATM")

    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            print(f"Available balance: ₹{balance:,.2f}")

        elif choice == "2":
            balance = withdraw(balance)

        elif choice == "3":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
