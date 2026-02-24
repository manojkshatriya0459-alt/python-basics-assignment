# Q17: Palindrome Checker
# This program checks if a word or number is a palindrome.
#
# Logic :
# - A palindrome reads the same forwards and backwards
# - Example: "racecar" -> forwards = racecar, backwards = racecar
# - For words: ignore case (treat uppercase and lowercase as same)
# - For numbers: just check digits
#
# Mathematicst:
# - reversed_string = original_string[::-1]
# - if original_string.lower() == reversed_string.lower() -> palindrome
# - else -> not palindrome
# - Show step-by-step: original, reversed, result

def palindrome_checker():
    # Step 1: Ask user for input
    text = input("Enter word/number: ")

    # Step 2: Store original
    original = text

    # Step 3: Reverse the string
    reversed_text = text[::-1]

    # Step 4: Check palindrome (ignore case for words)
    if original.lower() == reversed_text.lower():
        result = "PALINDROME"
    else:
        result = "NOT a palindrome"

    # Step 5: Show results
    print("\n=== PALINDROME CHECKER ===")
    print(f"Original: {original}")
    print(f"Reversed: {reversed_text}")
    print(f"Result: {result}")

# Step 6: Run the function
palindrome_checker()
