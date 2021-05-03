import random

random_number = random.randint(0, 100)

user_input = int(input("Pick a number between 0 to 100: "))

while 0 > user_input < 100:
    user_input = int(input("Pick a number between 0 to 100: "))


while user_input != random_number:
    if user_input > random_number:
        print(f"Your guess {user_input} is high")
    else:
        print(f"Your guess {user_input} is low")
    user_input = int(input("Pick a number between 0 to 100: "))
    
print(f"You guessed it right. Your guess of {user_input} is correct")