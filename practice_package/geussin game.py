import random
number = random.randint(5, 20)

counter = 0

while counter < 10:
    guessing_number = int(input("Enter a guessing number: "))
    if guessing_number == number:
        print("Congratulations you won!!!")
    else:
        print("Keep trying!!!", 9 - counter, "trials left")

    counter += 1
if counter == 10:
    print("Game Over!!!")
