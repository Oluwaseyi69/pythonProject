#number = input("Enter a code: ")
#while len(number) > 8:
    #number = input("Enter a code: ")
#print("Your password is secured, The lenght is", len(number))

for x in range(1, 13):
    print()
    for y in range(1, 13):
        print(f"{x} x {y} = {x*y}", end="\t\t")