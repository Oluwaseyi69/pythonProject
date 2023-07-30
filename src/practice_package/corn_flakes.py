no_of_student = 0
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
#for i in range(1, 2):
    #for j in range(1, 6):
        #print(f"{i}, {j}")


# for number in range(1, 11):
#
#     print(5 ** number, end=", ")



# number = 5
# for number in range(1, 10):
#     number = 5 ** number
#     print(number , end=", ")

# for g in range(10):
#      if g == 4:
#          continue
#      print(g)

# for x in range(20):
#     if x == 5:
#         continue
#     print(