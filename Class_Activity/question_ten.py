

def new_name(name, len)-> str:
    if len(name > 2):
        return name
    else:
        new_name(name, len)

name = new_name("seyi", 4)
print(name)


