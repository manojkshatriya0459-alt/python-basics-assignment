# Q19: Text Analysis Functions
# This program performs text analysis using multiple functions.
#
# Logic:
# - count_words(text): counts words by splitting text at spaces
# - count_vowels(text): counts vowels (a, e, i, o, u)
# - count_consonants(text): counts consonants (letters not vowels)
# - reverse_text(text): reverses the text
# - is_palindrome(text): checks if text reads same forwards and backwards
# - remove_vowels(text): removes vowels from text
# - word_frequency(text): counts how many times each word appears
# - longest_word(text): finds the longest word
# - analyze_text(text): calls all above functions and displays results
#
# Mathematics:
# - words = text.split()
# - vowels = count of characters in "aeiou"
# - consonants = count of letters not in vowels
# - reversed_text = text[::-1]
# - palindrome check: text.lower() == reversed_text.lower()
# - word frequency: dictionary with word counts
# - longest word: max(words, key=len)

def count_words(text):
    return len(text.split())

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

def count_consonants(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch.isalpha() and ch not in vowels)

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    return text.lower() == text[::-1].lower()

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(ch for ch in text if ch not in vowels)

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    lw = max(words, key=len)
    return lw, len(lw)

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print(f"Words: {count_words(text)}")
    print(f"Vowels: {count_vowels(text)}")
    print(f"Consonants: {count_consonants(text)}")
    print(f"Reversed: {reverse_text(text)}")
    print(f"Palindrome: {'Yes' if is_palindrome(text) else 'No'}")
    print(f"Without vowels: {remove_vowels(text)}")
# Run program
user_text = input("Enter text: ")
analyze_text(user_text)
