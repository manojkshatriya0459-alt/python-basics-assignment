# Q18: Calculator Functions
# This program creates a calculator using functions.
#
# Logic :
# - Define separate functions for each operation: add, subtract, multiply, divide, modulus, power
# - Main function (calculator) shows menu, takes user input, calls the right function, and shows result
# - Division must handle division by zero
# - Exit option ends the program
#
# Mathematics:
# - add(a, b) = a + b
# - subtract(a, b) = a - b
# - multiply(a, b) = a * b
# - divide(a, b) = a / b (only if b != 0)
# - modulus(a, b) = a % b (remainder when a is divided by b)
# - power(a, b) = a ^ b (a raised to the power b)

# Function definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero not allowed"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero not allowed"
    return a % b

def power(a, b):
    return a ** b

# Main calculator function
def calculator():
    while True:
        # Step 1: Show menu
        print("\n=== CALCULATOR MENU ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        # Step 2: Ask user for choice
        choice = int(input("Enter choice (1-7): "))

        if choice == 7:
            print("Exiting calculator. Goodbye!")
            break

        # Step 3: Ask for numbers
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        # Step 4: Perform operation
        if choice == 1:
            print(f"Result: {add(a, b)}")
        elif choice == 2:
            print(f"Result: {subtract(a, b)}")
        elif choice == 3:
            print(f"Result: {multiply(a, b)}")
        elif choice == 4:
            print(f"Result: {divide(a, b)}")
        elif choice == 5:
            print(f"Result: {modulus(a, b)}")
        elif choice == 6:
            print(f"Result: {power(a, b)}")
        else:
            print("Invalid choice. Please enter 1-7.")

# Step 5: Run the calculator
calculator()
