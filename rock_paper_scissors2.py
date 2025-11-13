import random
yes = True

while yes:
    print("--------Welcome to Rock, Paper, Scissors!--------")
    print("Choices: rock, paper, scissors")

    options = ("rock","paper","scissors")
    computer = random.choice(options)
    player = input("Enter your choice: ")
    
    if player not in  options:
        print("Invalid response")
        player = input("Enter your choice: ")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("🎉 You win! 🎉")
    else:
        print("🎉 Computer wins 🎉")
    print(f"The other player picked {computer}")
    play_again = input("Do you wanna play again(Y/N): ")
    if play_again == "Y":
        yes = True
    else:
        yes = False
        print("Thanks for playing! 👋.")