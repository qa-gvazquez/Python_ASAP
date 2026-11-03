"""
Tenemos un programa que calcula el Factorial de un número.

5! = 5 * 4 * 3 * 2 * 1
"""

def factorial(n):
    # Checking the number
    # is 1 or 0 then
    # return 1
    # otherwise return
    # factorial
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # Recursion

    # Driver Code
num = 5;
print("number : ", num)
print("Factorial : ", factorial(num))