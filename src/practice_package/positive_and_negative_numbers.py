positive_number = 0
negative_number = 0
counter = 1
total_positive = 0
total_negative = 0
total = 0
average_average = 0
number = int(input("Enter a number or 0 to end: "))

while number != 0:

    if number < 0:
        negative_number += number
        total_negative += negative_number
    if number > 0:
        positive_number += number
        total_positive += positive_number
        counter = counter + 1
        number = int(input("Enter a number or 0 to end: "))
        total = total_positive + total_negative
        average_average = total / counter
    if number == 0:
        print("the total is ", total, "\n\n", "the average is", average_average)
