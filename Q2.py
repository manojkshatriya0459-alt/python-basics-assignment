# Q2: Simple Calculator
# This program performs basic arithmetic operations based on user input.

# Mathematic:
# For two numbers a and b (using float data type to calculate in terms of decimal): 
# Addition: a + b 
# Subtraction: a - b 
# Multiplication: a * b 
# Division: a / b (b = 0), using if to display error if b is equal to zero
# Modulus: a%b, using if to display error if b is equal to zero
# Exponential: a**b

def calculator():
    # Step 1: Take inputs from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Step 2: Perform operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Division and modulus need if and else condition ,when num2 = 0 it causes a issue as mathematically its not possible to divide number by zero.
    if num2 != 0:
        division = num1 / num2
        modulus = num1 % num2
    else:
        division = "Error (division by zero)"
        modulus = "Error (modulus by zero)"

    exponentiation = num1 ** num2

    # Step 3: Display results in the required format
    print("\nResults:")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division }")
    print(f"{num1} % {num2} = {modulus}")
    print(f"{num1} ^ {num2} = {exponentiation}")

# Running the calculator(calling the function "calculator")
calculator()
