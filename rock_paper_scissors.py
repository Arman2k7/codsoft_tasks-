import random

VALID_CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def normalize_choice(choice):
    normalized = choice.strip().lower()
    if normalized not in VALID_CHOICES:
        raise ValueError("Please choose rock, paper, or scissors.")
    return normalized


def get_user_choice():
    while True:
        try:
            user_choice = input("Choose rock, paper, or scissors: ")
            return normalize_choice(user_choice)
        except ValueError as exc:
            print(exc)


def get_computer_choice():
    return random.choice(VALID_CHOICES)


def determine_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if BEATS[user_choice] == computer_choice:
        return "win"
    return "lose"


def display_result(user_choice, computer_choice, result):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if result == "tie":
        print("It is a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")


def play_game():
    print("Rock, Paper, Scissors")
    print("=====================")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_result(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)


if __name__ == "__main__":
    play_game()
