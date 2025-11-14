import random

"""This is a number guessing game"""
print("""Welcome to the Number Guessing Game. We have a number that needs to be guessed. You have 10 chances.
The secret number is 1 and 50
You have 10 attempts left.""")

Number = random.randint(1, 50)
#Number = 21

attempts = 10
Guess = False

num =1
while num <= 10:
    GuessNumber = int(input("Guess the number: "))
    if Number == GuessNumber:
        print("Congratulations ! You guessed the number!")
        Guess = True
        break
    else:
        if GuessNumber > Number:
            print("You guessed high number!")
        else:
            print("You guessed low number!")

    attempts = attempts - 1
    num = num + 1
    print("You have " + str(attempts) + " attempts left.")

if not Guess:
    print("Bad luck!")
print(f"Game Over!")
