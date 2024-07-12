# Hangman_Project
AiCore Project
Project title
Table of Content
Installation Instructions
import random
mkdir Hangman # type: ignore
git clone https://github.com/Onome1991/Hangman_Project.git

word_list= ['orange', 'mango', 'apple', 'cherin', 'banana']
print(word_list)
random.choice(word_list)
word= 'mango'
print(word)
len(word_list)
guess = input('E')
user_input = input("Please enter a single letter: ")
guess = user_input
if len(guess) == 1 and guess.isalpha():
    print("Good guess:")
else:
    print("Oops! That is not a valid input.")