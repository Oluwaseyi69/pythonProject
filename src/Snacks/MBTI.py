ei_response = [0, 0, 0, 0, 0, 0]


def name():
    # ei_response = 0
        user_input = input("Enter your name: ")
        if user_input == user_input:
                ei_response[0] = user_input


def question_one():

user_input = input("choose an option")


print("""
1). A. expand energy, enjoy groups \b B. Conserve energy, enjoy one-on-one""")
if user_input == "a":
    ei_response[1] = "A. Expand energy, enjoy groups"
elif user_input == "b":
    ei_response[1] = "B. Conserve energy, enjoy one-on-one"
else:
    print("Invalid choice")
