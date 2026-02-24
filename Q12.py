# Q12: Multiplication Table Generator
# This program asks the user for a number and a range, then prints the multiplication table.
#
# Logic:
# - User enters a number and a range (end value)
# - Program prints multiplication results from 1 up to that range
#
# Mathematics :
# - For each i from 1 to range:
#   result = number * i
# - Print in format: number x i = result
# - Print full multiplication table from 1 to 10 for all numbers 1 to 10 in grid format

def multiplication_table():
    # Step 1: Ask user for number and range
    number = int(input("Enter number: "))
    end_range = int(input("Enter range (end): "))

    # Step 2: Print multiplication table
    print(f"\nMultiplication Table of {number}")
    for i in range(1, end_range + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

def full_table_bonus():
    #Full multiplication table (1-10 for all numbers 1-10)
    print("\n=== FULL MULTIPLICATION TABLE (1 to 10) ===")
    # Print header row
    print("    ", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print()
    print("-" * 50)

    # Print table rows
    for i in range(1, 11):
        print(f"{i:2} |", end="")
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()

# Step 3: Run the function
multiplication_table()

# Step 4: Ask if user wants bonus full table
choice = input("\nDo you want to see the full table (1-10)? (yes/no): ").strip().lower()
if choice == "yes":
    full_table_bonus()
