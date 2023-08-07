def reversal(name) -> str:
    new_name = ""
    for index in name[len(name):: - 1]:
        new_name += index
    return new_name


name = "Seyi"
print(reversal(name))


def reverse(string):
    return string[:: -1]


name = "Hello"
print(reversal(name))
