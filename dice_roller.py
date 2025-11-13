# === Dice Roller Simulator ===

import random

def roll_dice():
    while True:
        input("Press Enter to roll the dice (or type 'quit' to exit): ")
        result = random.randint(1, 6)
        print("You rolled a", result)
        cont = input("Roll again? (y/n): ").lower()
        if cont != 'y':
            break

roll_dice()
