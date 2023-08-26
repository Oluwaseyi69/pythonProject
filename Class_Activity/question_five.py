
def reversal(name) -> str:
    return "".join(name[len(name):: - 1])


name = "Seyi Banwo"
print(reversal(name))