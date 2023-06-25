print("welcome to python")
first_name = input("Enter Firstname: ")
last_name = input("Enter Lastname: ")
age = int(input("Enter Age: "))
if first_name != "" and last_name != "":
    if age < 0:
        print(age, "Age cannot be empty")
    elif age < 18:
        print(age, "You are an underage")
    elif age > 65:
        print(age, "You are old")
elif first_name == "" and last_name == "":
    print("Both First Name and Last Name are empty")
elif first_name == "":
    print("First name is empty")
elif last_name == "":
    print("Last Name is empty")
else:
    print(f"Your name is {first_name} {last_name} and your age is {age}, you are a youth")
