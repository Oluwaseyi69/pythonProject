from LearnPyTest.Diaries import *

diaries = Diaries()
stored_username = ""


def main():
    welcome()
    new_account()


def welcome():
    print("""
        *************************************************************************
            Welcome to your Diary app, the ultimate digital diary journal app,
                we welcome to you with a sense of pride and Excitement.
        *************************************************************************
        """)


def new_account():
    print("""
    1. Create Diary Account
    2. Log in Existing Account
    3. Close
            """)

    user_input = input("Enter your preferred option: "'\n')
    if user_input == "1":
        create_account()
        # loading_successful()
    elif user_input == "2":
        login()
    else:
        print("Invalid Entry")
        new_account()


def create_account():
    username = input("kindly Enter your name: ""\n")
    password = input("Kindly Enter your password: ""\n")
    diaries.add_diary(username, password)

    print("Account Created Successfully")
    new_account()


def login():
    global stored_username
    try:
        print("Log in")
        username = input("Enter your username: ")
        password = input("Enter username and password: ")
        stored_username = username
        diaries.find_by_username(username).validate_password(password)
        options()
    except ValueError as error:
        print(error)
        new_account()


def options():
    global diaries
    print("""
            1) Add Entry
            2) Delete Entry
            3) Update Entry
            4) Find Entry
            5) Main Menu
            """)
    user_input = input("enter your preferred option")
    if user_input == "1":
        add_entry()
    elif user_input == '2':
        deleting_entry()
    elif user_input == '3':
        update_entry()
    elif user_input == '4':
        find_entry()
    elif user_input == '5':
        new_account()
    else:
        print("Invalid Entry")
        options()


def add_entry():
    try:
        title = input("Enter the title: ")
        body = input("Enter the content: ")

        diaries.find_by_username(stored_username) \
            .create_new_entry(title, body)
    except ValueError as error:
        print(error)
        add_entry()


def deleting_entry():
    try:
        entry_id = int(input("Enter Entry id: "))

        diaries.find_by_username(stored_username).delete_entry(entry_id)
    except ValueError as error:
        print(error)
        deleting_entry()

# def update


# def loading_successful():
#     print(">")
#     time.sleep(3)
#     print("Saved successfully")

# try:
#
#     username = input("Kindly Enter your Name: ""\n")
#     password = input("Kindly Input your password: ")
#     confirm_password = input("Kindly re-enter your password: ""\n")
#     if password == confirm_password:
#         print("you diary account opening is in process, Now you can proceed in creating memories")
#         main()
#
#     else:
#         print("password must match ")
#         create_account()
#
# except: IncorrectCredentialException("Enter a correct details")

if __name__ == '__main__':
    main()
