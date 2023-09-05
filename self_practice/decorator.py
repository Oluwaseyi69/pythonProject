
def design(x):
    print("=======")
    x()
    print("+++++++")
    return x


@design
def show():
    print("hello")