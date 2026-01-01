import random

def two_player_game():
    while True:
        print("\n-------- TWO-PLAYER MODE --------")
        print("Choices: rock, paper, scissors")

        valid_choices = ["rock", "paper", "scissors"]
        p1 = input("\nPlayer 1, what's your pick?: ").lower()
        p2 = input("Player 2, what's your pick?: ").lower()

        if p1 not in valid_choices or p2 not in valid_choices:
            print("❌ Invalid choice. Pick rock, paper, or scissors.")
        elif p1 == p2:
            print("🤝 It's a tie!")
        elif (
            (p1 == "rock" and p2 == "scissors") or
            (p1 == "paper" and p2 == "rock") or
            (p1 == "scissors" and p2 == "paper")
        ):
            print("🎉 Player 1 wins!")
        else:
            print("🎉 Player 2 wins!")

        choice = input("\n(1) Play again\n(2) Switch mode\n(3) Exit\nChoose: ")
        if choice == "1":
            continue
        elif choice == "2":
            return "SWITCH"
        else:
            return "EXIT"


def player_vs_computer():
    while True:
        print("\n-------- PLAYER VS COMPUTER MODE --------")
        print("Choices: rock, paper, scissors")

        options = ("rock", "paper", "scissors")
        computer = random.choice(options)
        player = input("Enter your choice: ").lower()

        while player not in options:
            print("Invalid response")
            player = input("Enter your choice: ").lower()

        print(f"Computer picked: {computer}")

        if (
            (player == "rock" and computer == "scissors") or
            (player == "paper" and computer == "rock") or
            (player == "scissors" and computer == "paper")
        ):
            print("🎉 You win!")
        elif player == computer:
            print("🤝 It's a tie!")
        else:
            print("🎉 Computer wins!")

        choice = input("\n(1) Play again\n(2) Switch mode\n(3) Exit\nChoose: ")
        if choice == "1":
            continue
        elif choice == "2":
            return "SWITCH"
        else:
            return "EXIT"


def main_game():
    mode_options = ("TWO PLAYER GAME", "PLAYER VS COMPUTER")

    print("-------- Welcome to Rock-Paper-Scissors --------")

    while True:
        mode = input("What mode do you want to play?: ").upper()

        while mode not in mode_options:
            print("Incorrect syntax")
            mode = input("What mode do you want to play?: ").upper()

        # Mode Loop
        while True:
            if mode == "PLAYER VS COMPUTER":
                result = player_vs_computer()
            else:
                result = two_player_game()

            if result == "SWITCH":
                # Flip mode
                if mode == "PLAYER VS COMPUTER":
                    mode = "TWO PLAYER GAME"
                    print("\n🔄 Switching to TWO-PLAYER mode…")
                else:
                    mode = "PLAYER VS COMPUTER"
                    print("\n🔄 Switching to PLAYER-VS-COMPUTER mode…")

            elif result == "EXIT":
                print("\nThanks for playing! 👋")
                return


# Run game
main_game()
