import re


def password_validator(password=input("Enter a password: ")):
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if len(password) < 8:
        return False
    if not re.search(r'[!@#$%^&*(),./?:{}[<>]', password):
        return False
    if not any(char.isdigit() for char in password):
        return False

    return True


# def passcode(code):
#     code = input("Enter a password")


if password_validator(password=input("Enter a password: ")):
    print("valid")
else:
    print("Invalid")
password_validator()
