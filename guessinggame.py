import random  # Import the random module to generate random numbers

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")  # Display a welcome message
print(" Bot have selected a number between 1 and 100. Can you guess it?")

# Initialize a variable to keep track of the number of attempts
attempts = 0

# Start a loop to allow the user to make multiple guesses
while True:
    guess = int(input("Enter your guess: "))  # Prompt the user to enter a guess
    attempts += 1  # Increment the number of attempts

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
        break  # Exit the loop since the user has guessed the correct number
    # Check if the guess is too high
    elif guess > secret_number:
        print("Too high! Try again.")
    # Check if the guess is too low
    else:
        print("Too low! Try again.")
