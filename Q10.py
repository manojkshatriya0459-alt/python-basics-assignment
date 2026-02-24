# Q10: Simple ATM Simulator
# This program simulates a simple ATM system with an initial balance of ₹10,000.
#
# Logic:
# - Show menu with options: Check Balance, Deposit, Withdraw, Exit
# - For deposit: add amount to balance
# - For withdrawal: check if balance is enough and minimum ₹500 must remain
# - For check balance: show current balance
# - Exit ends the program
#
# Mathematics:
# - deposit: balance = balance + deposit_amount
# - withdraw: balance = balance - withdraw_amount (only if balance - withdraw_amount >= 500)
# - check balance: just show balance
# - minimum balance rule: balance must always be >= 500

def atm_simulator():
    # Step 1: Set initial balance
    balance = 10000

    while True:
        # Step 2: Show menu
        print("\nATM SIMULATOR")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        # Step 3: Ask user for choice
        choice = int(input("Enter choice: "))

        # Step 4: Perform actions based on choice
        if choice == 1:
            # Check balance
            print(f"Your current balance is: ₹{balance}")

        elif choice == 2:
            # Deposit money
            amount = float(input("Enter amount to deposit: "))
            balance = balance + amount
            print(f"Deposit successful! New balance: ₹{balance}")

        elif choice == 3:
            # Withdraw money
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance - 500:
                balance = balance - amount
                print("Withdrawal successful!")
                print(f"New balance: ₹{balance}")
            else:
                print("Error: Insufficient balance or minimum ₹500 must remain.")

        elif choice == 4:
            # Exit program
            print("Thank you for using ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")

# Step 5: Run the function
atm_simulator()
