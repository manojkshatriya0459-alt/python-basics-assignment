# Q15: Prime Number Checker
# This program checks if a single number is prime (Part 1)
# and also finds all prime numbers in a given range (Part 2).
#
# Logic:
# - A prime number is greater than 1 and divisible only by 1 and itself
# - Special cases:
#   negative numbers, 0, and 1 are not prime
#   2 is the smallest prime number
#
# Mathematics:
# - To check if n is prime:
#   if n <= 1 -> not prime
#   if n == 2 -> prime
#   else check divisibility from 2 to sqrt(n) or up to n-1
#   if divisible by any number -> not prime
#   else -> prime
#
# - To find primes in a range:
#   loop through all numbers in range
#   check each number using prime logic
#   collect primes in a list

def is_prime(n):
    # Handle special cases
    if n <= 1:
        return False
    if n == 2:
        return True
    # Check divisibility
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_checker():
    # Part 1: Check single number
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")

    # Part 2: Find primes in a range
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)

    # Show results
    print("Prime numbers:", ", ".join(map(str, primes)))

# Run the function
prime_checker()
