"""
This is to practice Math Module.
"""

import math
number = float(input("Enter a number: "))
if number <= 0:
    print("Please enter a positive number")
else:
    sqrt = math.sqrt(number)
    print(f"The square root of {number} is {sqrt}")
    logx = math.log(number)
    print(f"The logarithm of {number} is {logx}")
    sin = math.sin(number)
    print(f"The sine of {number} is {sin}")