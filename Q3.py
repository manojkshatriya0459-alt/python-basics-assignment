# Q3: String Manipulator
# This program asks the user for a sentence and shows different results.
#
# Logic :
# - Count all characters including spaces using len(sentence)
# - Count all characters without spaces using len(sentence.replace(" ", ""))
# - Count how many words are in the sentence using len(sentence.split())
# - Change the sentence to uppercase using sentence.upper()
# - Change the sentence to lowercase using sentence.lower()
# - Change the sentence to title case using sentence.title()
# - Show the first word using words[0]
# - Show the last word using words[-1]
# - Reverse the sentence using sentence[::-1]
#
# Mathematics :
# - len(sentence) gives total characters (like counting each symbol one by one)
# - len(sentence.replace(" ", "")) removes spaces, then counts again
# - len(sentence.split()) counts words by splitting at spaces
# - sentence[::-1] reverses the string (like reading from last character to first)

def string_manipulator():
    # Step 1: Ask the user to type a sentence
    sentence = input("Enter a sentence: ")

    # Step 2: Do all the required operations

    # Original sentence
    original = sentence

    # Count characters including spaces
    chars_with_spaces = len(sentence)

    # Count characters without spaces
    chars_without_spaces = len(sentence.replace(" ", ""))

    # Count words by splitting sentence at spaces
    words = sentence.split()
    total_words = len(words)

    # Convert to uppercase
    uppercase = sentence.upper()

    # Convert to lowercase
    lowercase = sentence.lower()

    # Convert to title case
    title_case = sentence.title()

    # Get first word (if sentence is not empty)
    first_word = words[0] if words else ""

    # Get last word (if sentence is not empty)
    last_word = words[-1] if words else ""

    # Reverse the sentence
    reversed_sentence = sentence[::-1]

    # Step 3: Show all results
    print("\n=== STRING MANIPULATION RESULTS ===")
    print(f"Original: {original}")
    print(f"Characters (with spaces): {chars_with_spaces}")
    print(f"Characters (without spaces): {chars_without_spaces}")
    print(f"Words: {total_words}")
    print(f"UPPERCASE: {uppercase}")
    print(f"lowercase: {lowercase}")
    print(f"Title Case: {title_case}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Reversed: {reversed_sentence}")

# Step 4: Run the function
string_manipulator()
