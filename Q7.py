# Q7: Temperature Converter
# This program converts temperatures between Celsius, Fahrenheit, and Kelvin
# using a menu-based system.
#
# Logic explained in simple terms:
# - Show menu to user with choices
# - Ask for temperature value
# - Apply the correct formula based on choice
# - Show the converted result
#
# Mathematics behind it:
# - Celsius to Fahrenheit: (C * 9/5) + 32
# - Fahrenheit to Celsius: (F - 32) * 5/9
# - Celsius to Kelvin: C + 273.15
# - Kelvin to Celsius: K - 273.15
# - Fahrenheit to Kelvin: (F - 32) * 5/9 + 273.15
# - Kelvin to Fahrenheit: (K - 273.15) * 9/5 + 32

def temperature_converter():
    while True:
        # Step 1: Show menu
        print("\n=== TEMPERATURE CONVERTER ===")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        # Step 2: Ask user for choice
        choice = int(input("Enter your choice (1-7): "))

        # Step 3: Perform conversion based on choice
        if choice == 1:
            c = float(input("Enter temperature in Celsius: "))
            f = (c * 9/5) + 32
            print(f"{c} Celsius = {f:.2f} Fahrenheit")

        elif choice == 2:
            f = float(input("Enter temperature in Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f"{f} Fahrenheit = {c:.2f} Celsius")

        elif choice == 3:
            c = float(input("Enter temperature in Celsius: "))
            k = c + 273.15
            print(f"{c} Celsius = {k:.2f} Kelvin")

        elif choice == 4:
            k = float(input("Enter temperature in Kelvin: "))
            c = k - 273.15
            print(f"{k} Kelvin = {c:.2f} Celsius")

        elif choice == 5:
            f = float(input("Enter temperature in Fahrenheit: "))
            k = (f - 32) * 5/9 + 273.15
            print(f"{f} Fahrenheit = {k:.2f} Kelvin")

        elif choice == 6:
            k = float(input("Enter temperature in Kelvin: "))
            f = (k - 273.15) * 9/5 + 32
            print(f"{k} Kelvin = {f:.2f} Fahrenheit")

        elif choice == 7:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Step 4: Run the function
temperature_converter()