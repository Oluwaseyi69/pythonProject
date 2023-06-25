no_of_student = 1
sum = 0
counter = 0



while True:
    counter = counter + 1
    score = int(input("Enter a score or -25 to end: "))
    no_of_student += 1

    if score == -25:
        print("*************************************************************")
        print("        Aso Rock Secondary School, Abuja Nigeria    ")
        print("*************************************************************")
        print("Class: SSS3 ")
        print("Number of Student in class", no_of_student)
        print("Total score: ", sum)
        print("Average: ", average)
        print("*************************************************************")

        break
    else:
        sum = sum + score
        average = sum / counter
