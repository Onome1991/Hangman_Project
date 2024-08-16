# Step 1: Create a while loop that runs continuously
while True:
    # Step 2: Ask the user to guess a letter and assign it to the variable 'guess'
    guess = input("Guess a letter: ")
    
    # Step 3: Check that the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        # Step 4: If the guess passes the checks, break out of the loop
        break
    else:
        # Step 5: If the guess does not pass the checks, print an error message
        print("Invalid letter. Please, enter a single alphabetical character.")


import random

# Sample list of words to choose from
words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# Randomly select a secret word from the list
secret_word = random.choice(words)

while True:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ")
    
    # Check that the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        # Step 1: Create an if statement that checks if the guess is in the word
        if guess in secret_word:
            # Step 2: Print a message if the guess is correct
            print(f"Good guess! {guess} is in the word.")
            break  # Exit the loop after a correct guess, or continue as needed
        else:
            # Step 3: Print a message if the guess is incorrect
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

import random

# Sample list of words to choose from
words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# Randomly select a secret word from the list
secret_word = random.choice(words)

# Step 1: Define the check_guess function
def check_guess(guess):
    # Step 2: Convert the guess into lowercase
    guess = guess.lower()

    # Step 3: Check if the guess is in the word and provide feedback
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Step 1: Define the ask_for_input function
def ask_for_input():
    while True:
        # Step 2: Move the input validation code here
        guess = input("Guess a letter: ")
        
        # Check if the guess is a valid single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call check_guess to verify the guess
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Call the ask_for_input function to test the code
ask_for_input()

