PIN = "4321"
balance = 1000.00

attempts = 0

while attempts < 3:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == PIN:
        print("PIN accepted. Welcome!")
        break
    attempts += 1
    if attempts < 3:
        print("Incorrect PIN. Try again.")
    else:
        print("Card locked. Too many failed attempts.")
        raise SystemExit

while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print(f"Current balance: ${balance:.2f}")
    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            balance += amount
            print(f"Deposited ${amount:.2f}")
    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Withdrew ${amount:.2f}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
