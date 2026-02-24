# Q13: Sum and Average Calculator
# This program asks the user how many numbers they want to add.
# Then it takes that many numbers as input using a loop.
# It calculates sum, average, maximum, and minimum.
#
# Logic :
# - Ask user how many numbers
# - Use a loop to take that many inputs
# - Store numbers in a list
# - Calculate sum using sum(list)
# - Calculate average = sum / count
# - Find maximum using max(list)
# - Find minimum using min(list)
#
# Mathematics:
# - sum = number1 + number2 + ... + numberN
# - average = sum / N
# - maximum = largest number in the list
# - minimum = smallest number in the list

def sum_average_calculator():
    # Step 1: Ask user how many numbers
    count = int(input("How many numbers? "))

    # Step 2: Take inputs using loop
    numbers = []
    for i in range(1, count + 1):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)

    # Step 3: Do calculations
    total_sum = sum(numbers)
    average = total_sum / count
    maximum = max(numbers)
    minimum = min(numbers)

    # Step 4: Show results
    print("\n=== RESULTS ===")
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

# Step 5: Run the function
sum_average_calculator()
