height = float(input("Enter your height: "))
if height > 4.0:
    print("You are eligible to ride")
    age = float(input("How old are you: "))
    if 11 < age < 61:
        print("Kindly pay #200 to ride")
    elif age < 12:
        print(" Kindly pay #100 to ride ")
    elif age > 60:
        print("You are entitled to free ride")
else:
    print("You are too short")
