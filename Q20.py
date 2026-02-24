# Q20: Number System Functions
# This program provides multiple mathematical functions and a menu to test them.
#
# Logic :
# - factorial(n): multiply numbers from n down to 1
# - is_prime(n): check if divisible only by 1 and itself
# - fibonacci(n): nth Fibonacci number (0,1,1,2,3,5,...)
# - sum_of_digits(n): add all digits of the number
# - reverse_number(n): reverse the digits
# - is_armstrong(n): sum of each digit^number_of_digits == n
# - gcd(a, b): greatest common divisor using Euclidean algorithm
# - lcm(a, b): least common multiple using formula (a*b)/gcd(a,b)
# - is_perfect_number(n): sum of divisors (excluding n) == n
# - math_menu(): menu to call each function

def factorial(n):
    if n < 0:
        return "Error: Negative numbers not allowed"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n < 0:
        return "Error: Negative index not allowed"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

def reverse_number(n):
    return int(str(abs(n))[::-1]) if n >= 0 else -int(str(abs(n))[::-1])

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def is_perfect_number(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def math_menu():
    while True:
        print("\n=== MATH MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = int(input("Enter choice (1-10): "))

        if choice == 1:
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))
        elif choice == 2:
            n = int(input("Enter number: "))
            print(f"{n} is prime? {is_prime(n)}")
        elif choice == 3:
            n = int(input("Enter position (n): "))
            print(f"Fibonacci({n}) =", fibonacci(n))
        elif choice == 4:
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))
        elif choice == 5:
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))
        elif choice == 6:
            n = int(input("Enter number: "))
            print(f"{n} is Armstrong? {is_armstrong(n)}")
        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))
        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))
        elif choice == 9:
            n = int(input("Enter number: "))
            print(f"{n} is Perfect Number? {is_perfect_number(n)}")
        elif choice == 10:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-10.")

# Run the menu
math_menu()
