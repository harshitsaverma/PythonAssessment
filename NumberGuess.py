import random

"""This is a number guessing game"""
print("""Welcome to the Number Guessing Game. We have a number that needs to be guessed. You have 10 chances.
The secret number is 1 and 50
You have 10 attempts left.""")

Number = random.randint(1, 50)
GuessNumber = int(input("Guess the number: "))

for i in range(10,0,-1):
    if Number == GuessNumber:
        print("You guessed the number!")
        break
    elif GuessNumber > Number:
        print("You guessed too high!")
        print(f"You have {i-1} attempts left.")
        continue
    elif GuessNumber < Number:
        print("You guessed too low!")
        print(f"You have {i - 1} attempts left.")
        continue
print(f"Game Over!")
