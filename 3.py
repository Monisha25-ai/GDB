import random # Importing the random module
import sys # Importing the sys module for exiting the program
def continue_game():
    if input("Do you want to play again? (yes/no): ").lower() == "no":
        sys.exit()


# rock paper scissors game with counting wins , losses and ties
wins = 0
losses = 0
ties = 0

def continue_game():
    computer_choice = random.choice(["rock", "paper", "scissors"]) # Choosing a random choice for the computer
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower() # Getting user's choice
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1
        
