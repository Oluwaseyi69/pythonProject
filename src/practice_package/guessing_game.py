import random


def guessing_game(number):
    number = "4"

    guess_number = input("Enter a number: ")
    if guess_number == number:
        print("congratulations you won!!!")
    elif guess_number < "4":
        print("Too low try again")
    elif guess_number > "4":
        print("Too high try again")
    return guess_number == input("Enter a number: ")


solution = "5"
guessing_game(solution)
print(guessing_game(solution))



