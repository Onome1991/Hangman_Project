# Hangman_Project
AiCore Project
Project title
Table of Content
Project Title
Table of Contents, if the README file is long
A description of the project: what it does, the aim of the project, and what you learned
Installation instructions
Usage instructions
File structure of the project
License informationInstallation Instructions
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
    print("Oops! That is not a valid input.")codes
