number = int(input("Enter a number: "))

if number % 5 == 0 & number % 6 == 0:
    print(f"is {number} divisible 5 and 6 ? false")
elif number % 5 == 0 | number % 6 == 0:
    print(f" is {number} divisible by 5 or 6? true")
else:
    print(f"is {number} divisible by 5 or 6, but not both? true")
