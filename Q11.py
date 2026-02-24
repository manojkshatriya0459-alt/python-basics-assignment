# Q11: Number Pattern Printer
# This program prints different number patterns based on user choice and height.
#
# Logic :
# - User chooses which pattern (1 to 4)
# - User gives height (number of rows)
# - Program prints the chosen pattern using loops
#
# Mathematics :
# Pattern 1:
#   Row i prints numbers from 1 to i
# Pattern 2:
#   Row i prints the number i repeated i times
# Pattern 3:
#   Starts from height down to 1, each row prints numbers in reverse from that row down to 1
# Pattern 4:
#   Row i prints numbers from 1 up to i, then back down to 1 (like a pyramid)

def pattern_printer():
    # Step 1: Ask user for choice and height
    choice = int(input("Enter pattern choice (1-4): "))
    height = int(input("Enter height: "))

    print("\n=== NUMBER PATTERN ===")

    # Step 2: Print chosen pattern
    if choice == 1:
        # Pattern 1: increasing sequence
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif choice == 2:
        # Pattern 2: repeated numbers
        for i in range(1, height + 1):
            for j in range(i):
                print(i, end=" ")
            print()

    elif choice == 3:
        # Pattern 3: reverse decreasing sequence
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    elif choice == 4:
        # Pattern 4: pyramid style
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    else:
        print("Invalid choice. Please enter 1-4.")

# Step 3: Run the function
pattern_printer()
