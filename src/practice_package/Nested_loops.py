def stars(number):
    for y in range(0, number):
        for z in range(0, y + 1):
            print("*", end=" ")
        for x in range(number - y):
            print(" ", end=" ")
        for x in range(number - y):
            print("*", end=" ")
        for x in range(y):
            print(" ", end=" ")
        for z in range(1, y + 1):
            print(" ", end=" ")
        for z in range(number - y):
            print("*", end=" ")
        for x in range(number - y):
            print(" ", end=" ")
        for x in range(y):
            print("*", end=" ")
        print()


stars(10)
