while True:
    print("--------Welcome to Rock, Paper, Scissors!--------")
    print("Choices: rock, paper, scissors")

    valid_choices = ["rock", "paper", "scissors"]
    p1 = input("\nPlayer 1, what's your pick?: ").lower()
    p2 = input("Player 2, what's your pick?: ").lower()

    if p1 not in valid_choices or p2 not in valid_choices:
        print("❌ That’s not a valid choice. Pick rock, paper, or scissors.")
    elif p1 == p2:
        print("🤝 It's a tie!")
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        print("🎉 Player 1 wins!")
    else:
        print("🎉 Player 2 wins!")

    # ask to play again
    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! 👋")
        break



