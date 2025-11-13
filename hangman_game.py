# === Hangman Game ===

def hangman():
    word = "python"
    guesses = []
    max_attempts = 6
    attempts = 0

    print("=== Hangman Game ===")

    while attempts < max_attempts:
        display_word = ""
        for letter in word:
            if letter in guesses:
                display_word += letter
            else:
                display_word += "_"
        print("Word:", display_word)

        if display_word == word:
            print("You won!")
            break

        guess = input("Guess a letter: ").lower()
        if guess in guesses:
            print("You already guessed that.")
        elif guess in word:
            print("Correct guess!")
            guesses.append(guess)
        else:
            print("Wrong guess.")
            guesses.append(guess)
            attempts += 1
            print("Attempts left:", max_attempts - attempts)

    if attempts == max_attempts:
        print("Game over! The word was", word)

hangman()
