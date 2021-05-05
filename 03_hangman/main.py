import random
from words import words


# Pick a random word
def pick_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


word = pick_word()
guessed_letter = []

def hide_word(guessed_letter):
    hide = ""
    for letter in word:
        if letter in guessed_letter:
            hide = hide + letter
        else:
            hide = hide + "_"
    return hide



def remaining_guesses(guessed_letter, guess_no):
    if letter_input not in word:
        guess_no -= 1
    return guess_no

guess_no = 6
hide = hide_word(guessed_letter)

print(word)

while guess_no != 0:
    print(f"Word: {hide} & guessed letters: {guessed_letter} & remaining guesses: {guess_no}")
    

    # Display a message if letter was already guessed.
    while True:
        letter_input = input('Input your guessed letter: ')
        if letter_input in guessed_letter:
            print("Letter already guessed. Please input another letter")
        if letter_input not in guessed_letter:
            break

    guessed_letter.append(letter_input)

    

    # If guessed_letter in word, then display hide_word including this letter.
    hide = hide_word(guessed_letter)
    guess_no = remaining_guesses(letter_input, guess_no)

    if hide == word:
        print(f"You won! The word was {word}.")
        break

if hide != word:
    print(f"You lost. The word was {word}. Please try again later")
