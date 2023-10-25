# Name: Jon Person
# Assignment: Number Guessing Game
"""
Criteria: write a program to randomly choose a number between 1 and 100. The program should:
 1) Randomly choose a number between 1 and 100 (inclusive)
 2) Have the player enter a guess via input
 3) Tell the player the guess is high, low, or correct
 4) If high or low, allow the player to enter another guess
 5) Give the player an option to quit at any time
 6) Reward the player for a correct guess (ex., "Good job!")
 7) Tell the player how many guesses it took to guess correctly

"""

# import "random". This will give us a function that will allow us to choose a random integer.
import random

# Let's give our user a welcome message to start the game!
print("Get ready to guess the integer! Enter a number to see if it matches the random integer.")
print()
print("If you want to quit, enter 'q' at any time after you are prompted to guess a number.")
print()
print("Please press ENTER to continue.")
input()

# Next, let's define our number range from the instructions, 1-100
lower = 1
upper = 100

# This will record the number of guesses (duh); start number_of_guesses at 0
number_of_guesses = 0

# use random to generate a random integer, 1-100. Define it as "x"
x = random.randint(lower, upper)


# When the user guesses a number, then the code will look for the following conditions to be met
while True:
    # This defines 'guess' as a user input, with the prompt "Guess a number between 1 and 100: "
    guess = input("Guess a number between 1 and 100: ")
    # each time this loop starts again, 1 will be added to the number of guesses
    number_of_guesses += 1

# This allows a user to quit by entering 'q'
    if guess == 'q':
        print("Quitting Number Guessing Game. We hope you try again soon!")
        exit()

    # the 'try' function allows us to use exception handlers, so if the input is not an integer (like a letter) then
    # we can have it print an error message and continue instead of breaking the code
    try:
        # 'integer_guess' allows us to define our input 'guess' as an integer
        integer_guess = int(guess)
    except ValueError:
        print(f"Sorry, but {guess} is invalid. Your guess must be an integer between 1 and 100.")
        continue

    # If integer_guess is less than x, then it will return this error message and allow us to guess again
    if integer_guess < x:
        print(f"Oops! The number is larger than {guess}.")
    # If integer_guess is greater than x, then it will return this error message and allow us to guess again
    elif integer_guess > x:
        print(f"Oops! The number is smaller than {guess}.")
    # if they guess the correct number, then this will congratulate them and exit the program
    # it will also inform them of their number of guesses
    elif integer_guess == x:
        print(f"Congratulations, you guessed it in {number_of_guesses} tries! Thank you for playing.")
        exit()
