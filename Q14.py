# Q14: Factorial Calculator
# This program calculates the factorial of a number using a loop.
#
# Logic:
# - Factorial means multiplying the number by all smaller positive numbers down to 1
# - Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
# - Special case: 0! = 1
# - Negative numbers do not have factorial
#
# Mathematics:
# - n! = n × (n-1) × (n-2) × ... × 1
# - Loop from n down to 1 and multiply step by step
# - Show each step in the calculation

def factorial_calculator():
    # Step 1: Ask user for a number
    n = int(input("Enter a number: "))

    # Step 2: Handle negative numbers
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return

    # Step 3: Handle 0
    if n == 0:
        print("0! = 1")
        return

    # Step 4: Calculate factorial using loop
    factorial = 1
    steps = ""  # to store step-by-step calculation
    for i in range(n, 0, -1):
        factorial *= i
        if i == 1:
            steps += f"{i}"
        else:
            steps += f"{i} × "

    # Step 5: Show results
    print(f"\n{n}! = {steps} = {factorial}")

# Step 6: Run the function
factorial_calculator()
