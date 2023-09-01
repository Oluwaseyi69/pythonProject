import re


def name_entry():
    name = input("What is your name: ")
    if re.search("^(?!$)\D+$",name):
        print("Your name is "+ name)
    else:
        print("invalid name")
        name_entry()

name_entry()











def name_entry():
    name = input("What is your name: ")
    if name.isdigit():
        print("invalid name")
        name_entry()

    else:
        print(name)


name_entry()