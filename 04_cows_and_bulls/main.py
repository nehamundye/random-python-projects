"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
https://www.practicepython.org/exercise/2014/07/05/18-cows_count-and-bulls.html
"""

import random

# Generate a 4 digit number
def random_number():
    random_number = random.randint(1000, 9999)
    return int(random_number)

# convert the random number to a list
def number_list(number):
    number_list = []
    for digit in str(number):
        number_list.append(int(digit))
    return number_list

def bulls(list, mapped_index):
    new_list = []
    for i, elem in enumerate(list):
        if i not in mapped_index:
            new_list.append(elem)
    return new_list
 
if __name__=="__main__":
    print("Welcome to the Cows and Bulls Game! ")
    user_input = int(input("Enter a 4 digit number: "))
    random_number = random_number()
    random_number_list = number_list(random_number)
    guess_count = 1


    while user_input != random_number:
        user_input_list = number_list(user_input)

        # check for cows_count. 
        cows_count = 0
        mapped_index = []
        for i in range(0, len(user_input_list)):
            if user_input_list[i] == random_number_list[i]:
                cows_count += 1
                mapped_index.append(i)


        # check for bulls.
        bulls_count = 0
        if mapped_index:
            # create a new list for user_input_list and random_number_list excluding cows_count/mapped_index
            bulls_user_input_list = bulls(user_input_list, mapped_index)
            bulls_random_number_list = bulls(random_number_list, mapped_index)

            for elem in bulls_user_input_list:
                if elem in bulls_random_number_list:
                    bulls_count += 1

        
        print(f"{cows_count} cows and {bulls_count} bulls and guess count: {guess_count}")
        guess_count += 1
        user_input = int(input("Enter a 4 digit number: "))


    print(f"You won. The number was {random_number}. Your guess count: {guess_count}")