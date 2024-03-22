import random

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!", 0, 0
    elif (player == 'R' and computer == 'S') or \
         (player == 'S' and computer == 'P') or \
         (player == 'P' and computer == 'R'):
        return "You win!", 1, 0
    else:
        return "You lose!", 0, 1

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose R for rock, P for paper, or S for scissors: ").upper()
        while user_choice not in ['R', 'P', 'S']:
            print("Invalid choice. Please choose again.")
            user_choice = input("Choose R for rock, P for paper, or S for scissors: ").upper()

        choices = {'R': 'rock', 'P': 'paper', 'S': 'scissors'}
        computer_choice = random.choice(['R', 'P', 'S'])
        print(f"Your choice: {choices[user_choice]}")
        print(f"Computer's choice: {choices[computer_choice]}")

        result, user_score_delta, computer_score_delta = determine_winner(user_choice, computer_choice)
        print(result)

        user_score += user_score_delta
        computer_score += computer_score_delta

        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Game over!")
    print(f"Final scores are = Your score: {user_score}, Computer's score: {computer_score}")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()


main()
