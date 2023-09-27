import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_again():
    choice = input("Do you want to play again? (y/n): ")
    return choice.lower() == "y"

def print_choices(user_choice, computer_choice):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

def print_result(result):
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose!")

def print_scores(user_score, computer_score):
    print(f"\nScores - You: {user_score}  Computer: {computer_score}")

print("--- Rock-Paper-Scissors Game ---")

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    print("\nSelect your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice (1-3): ")
    user_choice = choices[int(user_choice) - 1]

    computer_choice = random.choice(choices)

    print_choices(user_choice, computer_choice)

    winner = determine_winner(user_choice, computer_choice)
    print_result(winner)

    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

    print_scores(user_score, computer_score)

    if not play_again():
        break

print("Thank you for playing Rock-Paper-Scissors!")