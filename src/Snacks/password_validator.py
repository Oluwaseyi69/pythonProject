import re

# password = input("Enter a password: ")
def password_validator():
    while True:
        password = input("Enter a password: ")

        if len(password) < 8:
            print("invalid password must have at least eight characters long")
            continue
        if not any(char.isupper() for char in password):
            print("invalid it must contain an uppercase")
            continue
        if not any(char.islower() for char in password):
            print("invalid password must have at least a lowercase")
            continue
        if not any(char.isdigit() for char in password):
            print("invalid it must have digit")
            continue

        return password


if password_validator():
    print("valid password")


# print(password)
    # if password == password_validator(password):
    #     print("valid")
    # elif password != password_validator(password):
    #     print("Invalid")


# def password_length(password):
#     password = input("enter a password")
#     while len(password) < 8:
#         if password == password_length(password):
#             print("valid ")
#         else:
#             print("invalid, try again")
# password = input("enter a password")
# password_length(password)

