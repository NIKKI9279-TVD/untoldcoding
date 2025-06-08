import random

def get_user_choice():
    choice = input("Choose Rock, Paper or Scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        choice = input("Choose Rock, Paper or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play():
    print("=== Rock Paper Scissors ===")
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    print(determine_winner(user, computer))

# Play multiple rounds
while True:
    play()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break
