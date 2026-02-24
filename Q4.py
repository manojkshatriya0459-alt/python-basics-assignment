# Q4: Age Calculator
# This program asks the user for their birth year and calculates:
# - Current age
# - Age in months
# - Age in days (approx 365 days per year)
# - Age in hours
# - Age in minutes
# - Years until age 100
#
# Mathematics:
# - age = current_year - birth_year
# - age_in_months = age * 12
# - age_in_days = age * 365
# - age_in_hours = age_in_days * 24
# - age_in_minutes = age_in_hours * 60
# - years_until_100 = 100 - age

def age_calculator():
    # Step 1: Ask the user for birth year
    birth_year = int(input("Enter your birth year: "))

    # Step 2: Get the current year (fixed here as 2026, you can change if needed)
    current_year = 2026

    # Step 3: Calculate age
    age = current_year - birth_year

    # Step 4: Calculate age in months, days, hours, minutes
    age_in_months = age * 12
    age_in_days = age * 365
    age_in_hours = age_in_days * 24
    age_in_minutes = age_in_hours * 60

    # Step 5: Calculate years until age 100
    years_until_100 = 100 - age

    # Step 6: Show results
    print("\n=== AGE CALCULATOR RESULTS ===")
    print(f"Current age: {age} years")
    print(f"Age in months: {age_in_months} months")
    print(f"Age in days (approx): {age_in_days} days")
    print(f"Age in hours: {age_in_hours} hours")
    print(f"Age in minutes: {age_in_minutes} minutes")
    print(f"Years until age 100: {years_until_100} years")

# Step 7: Run the function
age_calculator()
