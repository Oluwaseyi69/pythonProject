def multiply(number):
    for x in range(1, 13):
        print()
        for y in range(1, number):
            print(f"{x} x {y} = {x * y: <25}", end="\t\t")


multiply(30)
