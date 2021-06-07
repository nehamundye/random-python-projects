import random
import string
from words import words


class Hangman(object):
    def __init__(self, secret_word, num_of_guesses):
        self.num_of_guesses = num_of_guesses
        self.secret_word = secret_word
        self.guessed_letters = []

    def __str__(self):
        '''
        Returns string represenation of the secret word to be shown to user.
        '''
        display_string = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_string += letter
            else:
                display_string += "_"
        return display_string

    def is_winner(self):
        '''
        Returns True if user guessed the secret word, else return False.
        '''
        if str(self) == self.secret_word:
            return True
        return False

    def get_available_letters(self):
        '''
        Returns a string of available alphabets that a user can pick. (Subtracts all alphabets that a user have guessed already.)
        '''
        all_alphabets = list(string.ascii_lowercase)
        for letter in all_alphabets:
            if letter in self.guessed_letters:
                all_alphabets.remove(letter)
        available_letters = "".join(all_alphabets)
        return available_letters


def pick_random_word():
    '''
    Returns a random word from a list of words imported.
    '''
    secret_word = random.choice(words)
    while '-' in secret_word or ' ' in secret_word:
        secret_word = random.choice(words)
    return secret_word


if __name__ == '__main__':
    # Pick one secret word and display dash to the user. Show the total number of guesses the user has and available letters to guess the secret word. (Total number of guesses = 6)
    # Ask user for a letter he wants to guess. Validate the input.
    #   If the guessed letter is not in the secret word, reduce the number of guess by 1 and display to the user that the guessed letter was incorrect.
    #   If the guessed letter is in the secret word, keep the number of guesses as it is and display the letter in the word.
    #  The game ends when the user constructs the full word or runs out of guesses. 

    hangman = Hangman(pick_random_word(), 6)

    while hangman.num_of_guesses != 0:
        while True:
            print(f"You have {hangman.num_of_guesses} guesses left")
            print(f"Available letters: {hangman.get_available_letters()}")
            print(hangman)
            user_input = input("Please guess a letter: ")
            if user_input in hangman.guessed_letters:
                print("Letter already guessed. Please choose another letter\n")
            elif not user_input.isalpha() or len(user_input) > 1:
                print("Enter a valid letter (a-z)\n")
            elif len(user_input) == 1 and user_input.isalpha() and user_input not in hangman.guessed_letters:
                break

        hangman.guessed_letters.append(user_input)

        if user_input in hangman.secret_word:
            print("Good guess")
        elif user_input not in hangman.secret_word:
            hangman.num_of_guesses -= 1
            print("Oops, That letter is not in my word")
            print("#" * 19 + "\n")
            continue

        if hangman.is_winner():
            print("Congratulations, you won!")
            break
        print("#" * 29 + "\n")

    if not hangman.is_winner():
        print(f"Sorry, you ran out of guesses. The word was {hangman.secret_word}.")
