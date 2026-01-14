import random

def greetings ():
    print ("Hello, welcome to Day 4 programming!")
    print ("In this program we are going to build a simple number guessing game.")
    print("--------------------------------")



def number_guessing_game():
    greetings()
    computer_number = random.randint(1, 10)
    print(computer_number)
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess == computer_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry, you guessed {user_guess}. The correct number was {computer_number}.")


def normal_random():
    number_guessing_game()
    greetings()
    print("Generating a random float between 0.0 and 1.0:")
    random_float = random.random()
    print(random_float)

normal_random()

