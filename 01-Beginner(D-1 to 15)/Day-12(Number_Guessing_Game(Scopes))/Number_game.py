# import art
# import random
# print(art.logo)

# print("Welcome to the Number Guessing Game !")
# print("think of a number between 1 and 100.")

# level=input("Choose the Game Difficulty Level . Type 'easy' or 'hard ' : ").lower()

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
# answer=random.choice(numbers)
# print(answer)


# # IT IS THE LOGIC FOR OUR GUESS IS HIGH ,LOW OR CORRECT ?
# # guess=int(input("Make a guess: "))
# #
# # if guess > answer:
# #     print("You guessed too high")
# # elif guess < answer:
# #     print("You guessed too low")
# # else:
# #     print("You guessed correctly")

# #Easy
# if level == "easy":
#     attempts = 10
#     print(f"you have {attempts} attempts remaining to guess the number")
#     trying=True
#     while trying:
#         guess = int(input("Make a guess: "))

#         if guess > answer:
#             print("You guessed too high")
#             attempts=attempts -1
#             print(f"you have {attempts} attempts remaining to guess the number")
#         elif guess < answer:
#             print("You guessed too low")
#             attempts=attempts -1
#             print(f"you have {attempts} attempts remaining to guess the number")
#         else:
#             print("You guessed correctly")
#             trying=False


#         if attempts == 0:
#             print("You run out of guesses refresh and try again")
#             trying=False

# #Hard -exact same as easy but differs in no.of attempts
# elif level == "hard":
#     attempts = 5
#     print(f"you have {attempts} attempts remaining to guess the number")
#     trying = True
#     while trying:
#         guess = int(input("Make a guess: "))

#         if guess > answer:
#             print("You guessed too high")
#             attempts = attempts - 1
#             print(f"you have {attempts} attempts remaining to guess the number")
#         elif guess < answer:
#             print("You guessed too low")
#             attempts = attempts - 1
#             print(f"you have {attempts} attempts remaining to guess the number")
#         else:
#             print("You guessed correctly")
#             trying = False

#         if attempts == 0:
#             print("You run out of guesses refresh and try again")
#             trying = False

#---------------------Er style complete logic written by me ------------------------------

# But above code feels Too high lines we can shrink that using functions, because using loops also correct said by angela recall 

import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 and 100.")

level = input(
    "Choose the Game Difficulty Level. Type 'easy' or 'hard': "
).lower()


# ---------------------------------------------------------
# GENERATING THE ANSWER
# ---------------------------------------------------------

# Earlier, I created a list containing numbers 1 to 100
# and then used random.choice().
#
# But Python already has randint().
# randint(1, 100) directly gives us a random number
# between 1 and 100.

answer = random.randint(1, 100)

# Uncomment this while testing if you want to see the answer.
# print(answer)


# ---------------------------------------------------------
# FUNCTION 1 - CHECK THE GUESS
# ---------------------------------------------------------

# I created this function because the same guessing logic
# was being repeated in Easy and Hard mode.
#
# This function receives 3 things:
#
# guess    -> The number entered by the player
# answer   -> The actual random number
# attempts -> How many attempts are remaining
#
# The function will return TWO things:
#
# 1. Updated attempts
# 2. Whether the answer was correct or not


def check_guess(guess, answer, attempts):

    if guess > answer:

        print("You guessed too high")

        # One guess has been used.
        attempts = attempts - 1

        print(
            f"You have {attempts} attempts remaining to guess the number"
        )

        # False means the player has NOT guessed correctly.
        return attempts, False


    elif guess < answer:

        print("You guessed too low")

        # One guess has been used.
        attempts = attempts - 1

        print(
            f"You have {attempts} attempts remaining to guess the number"
        )

        # False means the player has NOT guessed correctly.
        return attempts, False


    else:

        print("You guessed correctly!")

        # We don't reduce attempts here because
        # the player has already won.

        # True means the player guessed correctly.
        return attempts, True


# ---------------------------------------------------------
# FUNCTION 2 - PLAY THE GAME
# ---------------------------------------------------------

# Instead of writing the entire game twice:
#
# Easy -> 10 attempts
# Hard -> 5 attempts
#
# We create the game only ONCE.
#
# Then we simply give the function a different number:
#
# play_game(10)
# play_game(5)


def play_game(attempts):

    print(
        f"You have {attempts} attempts remaining to guess the number"
    )

    # Keep running the game while attempts are greater than 0.
    while attempts > 0:

        guess = int(input("Make a guess: "))


        # check_guess() returns TWO values:
        #
        # attempts -> updated number of attempts
        # correct  -> True or False
        #
        # Example:
        #
        # return 9, False
        #
        # becomes:
        #
        # attempts = 9
        # correct = False

        attempts, correct = check_guess(
            guess,
            answer,
            attempts
        )


        # If the player guessed correctly,
        # stop the game.
        if correct:
            break


        # If attempts reached zero,
        # the player has lost.
        if attempts == 0:

            print("You ran out of guesses. Refresh and try again.")

            break


# ---------------------------------------------------------
# START THE GAME
# ---------------------------------------------------------

# If the player selected Easy,
# give them 10 attempts.

if level == "easy":

    play_game(10)


# If the player selected Hard,
# give them 5 attempts.

elif level == "hard":

    play_game(5)