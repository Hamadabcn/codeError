# A function to calculate the factorial of a positive integer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# A function to print the first n terms of the Fibonacci sequence
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# A function to check if a string is a palindrome
def palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

# Test the functions
print(factorial(5))
fibonacci(10)
print(palindrome("racecar"))
