import random


while True:

    Name = input("Enter your name: ")
    print(f"Welcome, {Name}!")

    computer_number = random.randint(1, 10)
    print(computer_number)
    user_guess = int(input("Guess a number between 1 and 10: "))

    if user_guess == computer_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print(f"Sorry, you guessed {user_guess}. The correct number was {computer_number}.")