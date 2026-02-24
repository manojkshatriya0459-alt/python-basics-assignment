# Q5: Bill Splitter
# This program calculates how a restaurant bill is split among people.
#
# Logic:
# - Take inputs: total bill, number of people, tax percentage, tip percentage
# - Calculate tax amount = (subtotal * tax_percentage) / 100
# - Calculate bill after tax = subtotal + tax_amount
# - Calculate tip amount = (bill_after_tax * tip_percentage) / 100
# - Calculate total bill = bill_after_tax + tip_amount
# - Calculate amount per person = total_bill / number_of_people

def bill_splitter():
    # Step 1: Ask for inputs
    subtotal = float(input("Enter total bill: "))
    people = int(input("Number of people: "))
    tax_percent = float(input("Tax percentage: "))
    tip_percent = float(input("Tip percentage: "))

    # Step 2: Do the calculations
    tax_amount = (subtotal * tax_percent) / 100
    bill_after_tax = subtotal + tax_amount
    tip_amount = (bill_after_tax * tip_percent) / 100
    total_bill = bill_after_tax + tip_amount
    amount_per_person = total_bill / people

    # Step 3: Show the results
    print("\n=== BILL BREAKDOWN ===")
    print(f"Subtotal:    ₹{subtotal:.2f}")
    print(f"Tax ({tax_percent}%):   ₹{tax_amount:.2f}")
    print(f"After tax:   ₹{bill_after_tax:.2f}")
    print(f"Tip ({tip_percent}%):   ₹{tip_amount:.2f}")
    print(f"Total:       ₹{total_bill:.2f}")
    print(f"Per person:  ₹{amount_per_person:.2f}")

# Step 4: Run the function
bill_splitter()
