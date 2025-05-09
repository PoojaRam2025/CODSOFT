import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    print("\n--- ROCK PAPER SCISSORS ---")
    user = input("Choose rock, paper, or scissors (or 'exit' to stop): ").lower()

    if user == 'exit':
        break

    if user not in choices:
        print("Invalid choice.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
        print("You win!")
        user_score = user_score + 1
    else:
        print("Computer wins!")
        computer_score = computer_score + 1

    print("Score: You", user_score, "- Computer", computer_score)
