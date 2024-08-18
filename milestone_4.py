import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Step 3: Initialize the attributes
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

# Example usage
if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
    game = Hangman(word_list)
    print(f"The word to guess: {game.word}")
    print(f"Word guessed so far: {game.word_guessed}")
    print(f"Number of unique letters: {game.num_letters}")
    print(f"Number of lives: {game.num_lives}")
    print(f"List of guesses: {game.list_of_guesses}")

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    # Step 1: Define the check_guess method
    def check_guess(self, guess):
        # Convert the guessed letter to lower case
        guess = guess.lower()

        # Check if the guess is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Here we could add logic later to update word_guessed, but that's for later tasks
        else:
            print(f"Sorry, {guess} is not in the word.")

    # Step 2: Define the ask_for_input method
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            # Check if the guess is NOT a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            # Check if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            
            # If the guess is valid and not already guessed
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Step 3: Test the code
if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
    game = Hangman(word_list)
    game.ask_for_input()

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    # Step 1: Define the check_guess method
    def check_guess(self, guess):
        # Convert the guessed letter to lower case
        guess = guess.lower()

        # Check if the guess is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Step 2: Update word_guessed with the correct guess
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            
            # Reduce the number of unique letters left to guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")

    # Step 2: Define the ask_for_input method
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            # Check if the guess is NOT a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            # Check if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            
            # If the guess is valid and not already guessed
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Step 3: Test the code
if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
    game = Hangman(word_list)
    game.ask_for_input()
    print(f"Word guessed so far: {game.word_guessed}")
