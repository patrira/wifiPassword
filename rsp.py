import random

# Define the choices available in the game
choices = ['rock', 'paper', 'scissors']

# Prompt the user to input their choice
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Generate a random choice for the computer
computer_choice = random.choice(choices)

# Display the choices made by the user and the computer
print("You chose:", user_choice)
print("Computer chose:", computer_choice)

# Determine the winner based on the choices
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 'rock':
    if computer_choice == 'scissors':
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == 'paper':
    if computer_choice == 'rock':
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == 'scissors':
    if computer_choice == 'paper':
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice! Please choose between rock, paper, or scissors.")
