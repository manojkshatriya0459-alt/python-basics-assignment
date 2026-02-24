# Q9: Ticket Pricing System
# This program calculates movie ticket prices based on age, day of week, and number of tickets.
#
# Logic:
# - Age decides base price:
#   below 3 = free
#   3 to 12 = 150 (child)
#   13 to 59 = 300 (adult)
#   60 and above = 200 (senior)
# - Day decides discount:
#   Monday to Thursday = no discount
#   Friday to Sunday = 20 percent discount
# - Total price = (base price * number of tickets) - discount
#
# Mathematics:
# - base_price is chosen based on age
# - subtotal = base_price * tickets
# - discount = (subtotal * 20) / 100 if day is Friday, Saturday, or Sunday
# - price_after_discount = subtotal - discount
# - total_amount = price_after_discount

def ticket_pricing_system():
    # Step 1: Ask for inputs
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").strip().lower()
    tickets = int(input("Enter number of tickets: "))

    # Step 2: Decide base price based on age
    if age < 3:
        base_price = 0
        category = "Free"
    elif 3 <= age <= 12:
        base_price = 150
        category = "Child"
    elif 13 <= age <= 59:
        base_price = 300
        category = "Adult"
    else:
        base_price = 200
        category = "Senior"

    # Step 3: Calculate subtotal
    subtotal = base_price * tickets

    # Step 4: Calculate discount based on day
    if day in ["friday", "saturday", "sunday"]:
        discount = (subtotal * 20) / 100
    else:
        discount = 0

    # Step 5: Calculate price after discount and total amount
    price_after_discount = subtotal - discount
    total_amount = price_after_discount

    # Step 6: Show results
    print("\n=== TICKET PRICE BREAKDOWN ===")
    print(f"Category: {category}")
    print(f"Base price per ticket: ₹{base_price:.2f}")
    print(f"Number of tickets: {tickets}")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Price after discount: ₹{price_after_discount:.2f}")
    print(f"Total amount: ₹{total_amount:.2f}")

# Step 7: Run the function
ticket_pricing_system()
