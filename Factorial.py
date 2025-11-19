"""
This is the program to get factorial of numbers
"""

num = input("Enter a number: ")
def factorial(num):
    fact = 1
    if num in (0, 1):
        return fact
    elif num < 0 :
        print("The factorial of a negative integer is not defined. Kindly use positive number.")
    else:
        fact = num * factorial(num -1)
        return fact


print(f"Factorial of {num} is {factorial(int(num))}")
