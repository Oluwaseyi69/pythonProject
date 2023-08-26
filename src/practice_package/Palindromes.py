def word()-> bool:
    user_input = str(input("Enter a name: "))
    for x in user_input:
        if user_input == (user_input -1) :
            return True
        else:return False

word()