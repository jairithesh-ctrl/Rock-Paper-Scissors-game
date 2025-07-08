import random

options = ['rock', 'paper', 'scissors']

# Get number of rounds
rounds = int(input("How many rounds do you want to play? "))

user_score = 0
computer_score = 0

for i in range(rounds):
    print(f"\nRound {i + 1}")
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice! You lose this round by default.")
        computer_score += 1
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print("\nGame Over!")
print(f"Your score: {user_score}")
print(f"Computer score: {computer_score}")

if user_score > computer_score:
    print("Congratulations, you won the game!")
elif user_score < computer_score:
    print("Computer won the game! Better luck next time.")
else:
    print("The game is a tie!")

