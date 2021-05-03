import random

while True:
    user_secret_number = int(input("Pick a number between 0 to 100: "))
    if user_secret_number >=0 and user_secret_number <=100:
        break

# Define new_high and new_low numbers to go as a paramater inside randint(new_low, new_high)
new_low = 0
new_high = 100

#show this random_number to user and ask it is too high, too low or correct
answer_option = ['c', 'l', 'h']

user_input = 'k'
random_number = -1


while user_secret_number != random_number:
    # Computer will guess a random number between new_low and new_high
    random_number = random.randint(new_low, new_high)
    
    while True:
        user_input = input(f"Is the number {random_number}?, Enter c for correct or h for high or l for low?: ")
        if user_input in answer_option:
            break


    if user_input == "h":
        new_high = random_number - 1
    elif user_input == "l":
        new_low = random_number + 1 

print(f"Computer guessed it right. Your secret number is {random_number}")

