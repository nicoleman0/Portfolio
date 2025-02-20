# create a greeting
# create a list of words
# randomly select a word from the list
# ask the user to guess a letter
# bonus - take input from user and make it lowercase
# check if the letter is in the word

import random

def greeting():
    print("Welcome to Hangman: Programming Edition!")
    print("Try to guess the word one letter at a time.")
    print("Good luck!")

word = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php', 'csharp', 'c', 'cplus']
random_word = random.choice(word)

greeting()

guessed_letters = []
attempts = 6

while attempts > 0:
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in random_word:
        print(f"Good guess! The letter {guess} is in the word.")
    else:
        attempts -= 1
        print(f"Sorry, the letter {guess} is not in the word. You have {attempts} attempts left.")
    
    # Display the current state of the word
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in random_word])
    print(display_word)
    
    if '_' not in display_word:
        print("Congratulations! You've guessed the word!")
        break
else:
    print(f"Game over! The word was {random_word}.")
