# === Guess the Number Game ===

import random

def guess_number():
    secret = random.randint(1, 50)
    attempts = 0
    guess = 0

    print("=== Guess the Number ===")

    while guess != secret:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print("🎉 You got it in", attempts, "attempts!")

guess_number()
