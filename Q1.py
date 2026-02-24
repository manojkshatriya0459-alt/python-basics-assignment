# Q1: Personal Bio Card
# This program accepts student details from the user and displays the card


def bio_card():
    # Step 1: Accept details from the user
    # Each input is stored in a variable
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))   # age inform of integer
    course = input("Enter your course: ")
    college = input("Enter your college: ")
    email = input("Enter your email: ")

    # Step 2: Display the card after all inputs are collected
    # Using f-strings for clean formatting
    print("\n=== STUDENT BIO CARD ===")
    print(f"Name    : {name}")
    print(f"Age     : {age}")
    print(f"Course  : {course}")
    print(f"College : {college}")
    print(f"Email   : {email}")

# Step 3: Call the function to run the program
bio_card()

