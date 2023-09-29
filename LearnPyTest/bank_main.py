# import bank
import self
from LearnPyTest.bank import Bank

from LearnPyTest.bank import Bank


def welcome():
    print("Welcome to Shebotimo Bank")
    display()


def display():
    print("""
        1-> Create Account
        2-> Deposit 
        3-> Withdraw
        4-> Exit
    """)
    user_input = input("Kindly enter a number: ")
    if user_input == "1":
        create_account()
    elif user_input == "2":
        deposit_cash()
    elif user_input == "4":
        exit()


def create_account():
    first_name = input("Enter Your First Name: ")
    last_name = input("Enter your Last Name: ")
    pin = input("Enter your pin: ")
    account_created = bank.register(first_name, last_name, pin)
    account = account_created.get_account_number()
    print(f"""
    ************************************************
            Welcome to Shebotimo bank,
            Account Successfully Created
            Account name:  {first_name} {last_name}
            Account number: {account}
    ************************************************
            Thank you for Banking with us.
    ************************************************
    """)
    enquire()


def enquire():
    print(""" 
    Do you like to perform more transaction? 
    
    1-> Back to Main Menu
    2-> Exit
    """)
    response = int(input("enter a number: "))
    if response == 1:
        display()
    elif response == 2:
        exit()

    else:
        print("invalid input")


def deposit_cash():
    receivers_account_num = int(input("kindly enter your account number: "))
    receivers_name = input("Kindly enter your name: ")
    amount = int(input("Enter your amount: "))
    bank.deposited(amount, receivers_account_num)
    print(
        f"""
    ************************************************
        Hello {receivers_name}
        Your account number {receivers_account_num}
        Has been credited with {amount}
    ************************************************
    
    """
    )




if __name__ == '__main__':
    bank = Bank("Ab Bank", "pin")
    welcome()
