#
# def email_validator(email : list):
#     if email.endswith("char." and "char >1"):
#         return False
#     if email.startswith("@"):
#         return False
#     return False if email.__contains__("@") else False
#
#
# email = ["seyi001@gmail.com"]
# if email_validator(email):
#     print("Valid")
# else:
#     print("Invalid")
import re


# import re
#
#
# def is_valid_email(email: list):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     if re.match(pattern, email):
#         return True
#     else:
#         return False
#
#
# email = ["Seyi@001", "Seyi@1","ddddSt5@"]
#
# if is_valid_email(email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")

def email_validator():
    valid = []
    counter = 0

    while counter < 5:
        email = input("Enter your email address")
        if email.startswith(".com") or email.endswith("@"):
            print("Invalid email")

        elif email.startswith(".it"):
            print("Invalid email")
        elif email.startswith(".africa"):
            print("Invalid email")
        elif re.match(r"^[@]+@[@]+\.[^@]+", email):
            valid.append(email)
        elif email.endswith(".com"):
            valid.append(email)
        elif email.endswith(".it"):
            valid.append(email)
        elif email.endswith(".africa"):
            valid.append(email)

    return valid


if __name__ == '__main__':
    valid = email_validator()

print("Valid email", valid)
