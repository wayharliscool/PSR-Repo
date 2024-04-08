import random

options = ("rock", "paper", "scissors", "human", "robot")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors, human, robot): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "human" and computer == "scissors":
        print("You win!")
    elif player == "robot" and computer == "human":
        print("You win!")
    elif player == "rock" and computer == "human":
        print("You win!")
    elif player == "paper" and computer == "robot":
        print("You win!")
    elif player == "scissors" and computer == "robot":
        print("You win!")
    elif player == "human" and computer == "paper":
        print("You win!")
    elif player == "robot" and computer == "rock":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")