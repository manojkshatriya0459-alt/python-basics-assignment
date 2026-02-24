# Q8: Leap Year Checker
# This program checks if a given year is a leap year.
#
# Logic :
# - A year is a leap year if:
#   divisible by 4 AND (not divisible by 100 OR divisible by 400)
#
# Mathematics :
# - year % 4 == 0 means year is divisible by 4
# - year % 100 == 0 means year is divisible by 100
# - year % 400 == 0 means year is divisible by 400
# - Rule: leap year if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def leap_year_checker():
    # Step 1: Ask user for a year
    year = int(input("Enter a year: "))

    # Step 2: Apply leap year rules
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        result = "Leap year"
        reason = "Divisible by 4 and (not divisible by 100 or divisible by 400)"
    else:
        result = "NOT a leap year"
        reason = "Either not divisible by 4 or divisible by 100 but not by 400"

    # Step 3: Show results
    print("\n=== LEAP YEAR CHECKER ===")
    print(f"Year: {year}")
    print(f"Result: {result}")
    print(f"Reason: {reason}")

# Step 4: Run the function
leap_year_checker()
